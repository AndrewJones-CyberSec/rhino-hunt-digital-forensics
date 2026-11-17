# Case-specific post-examination verification of public DFRWS training captures.
# Run from the repository root with copies of the captures in upload/.
import struct, socket, collections, pathlib, datetime, re, hashlib
for p in sorted(pathlib.Path('upload').glob('rhino*.log')):
    b=p.read_bytes(); pos=24; idx=0; origin=None; streams=collections.defaultdict(list); print('\n',p.name,len(b))
    while pos+16<=len(b):
        sec,usec,caplen,length=struct.unpack_from('<IIII',b,pos); pos+=16; frame=b[pos:pos+caplen];pos+=caplen;idx+=1
        if origin is None: origin=sec+usec/1e6; print('first UTC',datetime.datetime.fromtimestamp(origin,datetime.timezone.utc))
        if len(frame)<54 or frame[12:14]!=b'\x08\x00': continue
        ip=frame[14:]; ihl=(ip[0]&15)*4
        if ip[9]!=6: continue
        src,dst=socket.inet_ntoa(ip[12:16]),socket.inet_ntoa(ip[16:20]); tcp=ip[ihl:struct.unpack_from('!H',ip,2)[0]]
        if len(tcp)<20: continue
        sp,dp,seq=struct.unpack_from('!HHI',tcp); data=tcp[(tcp[12]>>4)*4:]
        if not data: continue
        streams[(src,sp,dst,dp)].append((seq,idx,data))
        if sp==21 or dp==21:
            for l in data.splitlines():
                if re.match(rb'(STOR |RETR |230 |226 |USER )',l): print(idx,round(sec+usec/1e6-origin,6),src,sp,'->',dst,dp,l[:140])
        if dp==80 and re.match(rb'GET /~gnome',data): print(idx,src,'->',dst,data.splitlines()[0][:160])
    print('packets',idx,'last UTC',datetime.datetime.fromtimestamp(sec+usec/1e6,datetime.timezone.utc))
    for key,items in streams.items():
        if 21 in (key[1],key[3]) or 23 in (key[1],key[3]): continue
        chunks=sorted(items); curr=chunks[0][0]; data=b''
        for seq,i,chunk in chunks:
            if seq>curr: break
            offset=max(0,curr-seq); data+=chunk[offset:];curr=max(curr,seq+len(chunk))
        for magic, label in [(b'\xff\xd8\xff','JPEG'),(b'GIF89a','GIF'),(b'GIF87a','GIF'),(b'PK\x03\x04','ZIP'),(b'MZ\x90\x00','PE')]:
            at=data.find(magic)
            if at==0 and key[3]==20: print('FTP object',label,'stream',key,'bytes',len(data),'frame',chunks[0][1],'SHA256',hashlib.sha256(data).hexdigest())
        if key[0]=='137.30.120.37' and key[1]==80:
            for m in re.finditer(rb'HTTP/1\.[01] 200 OK\r\n(.*?)\r\n\r\n',data,re.S):
                h=m.group(1); size=re.search(rb'(?i)Content-Length:\s*(\d+)',h); typ=re.search(rb'(?i)Content-Type:\s*([^\r\n]+)',h)
                if size and typ and int(size[1])>50000:
                    n=int(size[1]); body=data[m.end():m.end()+n]; print('HTTP object',typ[1],key,'size',len(body),'expected',n,'SHA256',hashlib.sha256(body).hexdigest(),'header',body[:4].hex())

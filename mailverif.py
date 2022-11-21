from asyncio.timeouts import timeout
import aiosmtplib
import dns.resolver

records = dns.resolver.Resolver().resolve(mailProvider, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)

try :
    server= aiosmtplib.esmtp.ESMTP(timeout=10)
    await server.connect(hostname=mxRecord)
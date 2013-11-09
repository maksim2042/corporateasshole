DNB_TOKEN = 'WLSSzjRE0MfyxnZhTA6YZ4gyufsHftl7sUfdvaUAq863tIgGxtTrMEPW0hNWSujEA2E86rC5CG+6LK3DnmoPdWk+kdCqz8oNpxNugMpbCVU4W05kr/RQwCcwvaya4IOxzXwByaERVMoZUL9EH3es3f78njZ6G2locOwKTpafT0P3/MHjAhJZ7qG/Yuw9onKm8lAx+DR7/+USbOn1evyNzNLXYQW585VDYWar3uO8F3GRdM821RkKwYOcX2SXLCvfAWBbEHqgPaipRWdd5qlTRYf+lyCqpOy9JUJ9wCBCOvucfl6p6++e+sZ/3M3Kx53jGAM/x6TcuWcjxCCsr0ag4g=='



import socket

CRSF_ENABLED = True
SECRET_KEY = 'devkey'
RECAPTCHA_PUBLIC_KEY = '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'
PORT='8888'

if socket.gethostname().startswith('gella'):
    print("configuring for Localhost")
    MONGO_URI = 'mongodb://localhost:27018/corp_ahole'
else:
    print("configuring for deploy")
    MONGO_URI = 'mongodb://localhost:27017/corp_ahole'
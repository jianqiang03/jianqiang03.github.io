"""Fetch fixed paper versions and extract text; requires requests and pdftotext."""
import concurrent.futures,json,hashlib,subprocess
from pathlib import Path
import requests
P=Path(__file__).resolve().parent/'sources'
P.mkdir(parents=True, exist_ok=True)
ids={'scaling':'2602.09722v1','quality':'2610.18869v1','molmoact2':'2605.02881v1','openvla':'2406.09246v1','foundry':'2604.19728v1'}
def one(kv):
 k,v=kv;u='https://arxiv.org/pdf/'+v;p=P/(k+'.pdf');r=requests.get(u,timeout=120);r.raise_for_status();assert r.content.startswith(b'%PDF');p.write_bytes(r.content);subprocess.run(['pdftotext','-layout',str(p),str(P/(k+'.txt'))],check=True);return k,{'url':u,'sha256':hashlib.sha256(r.content).hexdigest(),'bytes':len(r.content)}
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex:d=dict(ex.map(one,ids.items()))
(P/'manifest.json').write_text(json.dumps(d,indent=2));print(d)

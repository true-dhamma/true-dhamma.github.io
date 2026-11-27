import sys,json,glob,importlib,subprocess,os
D='/workspace/reader-work/m-review-reader-13'; sys.path.insert(0,D)
R='/workspace/true-dhamma'; BASE='e0478db'
texts={}
def get(f):
    if f not in texts:
        texts[f]=subprocess.run(['git','-C',R,'show',f'{BASE}:_buddhadhamma/{f}'],capture_output=True,text=True).stdout
    return texts[f]
log=[];bad=0
files=sorted(glob.glob(D+'/p[12]_*.py'),key=lambda p:(p.split('/')[-1][:2],int(p.split('_')[-1][:-3])))
for n in files:
    mod=n.split('/')[-1][:-3]; m=importlib.import_module(mod); ps=mod[:2]
    for e in m.P:
        f,cat,old,new,why=e[:5]; cnt=e[5] if len(e)>5 else 1
        t=get(f); k=t.count(old)
        if k!=cnt: print('BAD',mod,f,cat,k,cnt,old[:50]); bad+=1; continue
        line=t[:t.index(old)].count('\n')+1
        assert old.count('\n')==new.count('\n'),(mod,old[:30])
        texts[f]=t.replace(old,new)
        log.append({'id':f'R13-{len(log)+1:04d}','pass':ps,'file':f,'cat':cat,'line':line,'old':old,'new':new,'why':why,'count':cnt})
if bad: sys.exit(1)
if '--write' in sys.argv:
    for f,t in texts.items(): open(f'{R}/_buddhadhamma/{f}','w').write(t)
json.dump(log,open(D+'/applied.json','w'),ensure_ascii=False,indent=1)
import collections
print(len(log),'ok',dict(collections.Counter((e['pass'],e['file']) for e in log)))

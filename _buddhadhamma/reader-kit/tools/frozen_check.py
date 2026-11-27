#!/usr/bin/env python3
"""Reader 批次冻结项校验：比较 base(git rev) 与工作区 43MD。只读。
用法: frozen_check.py <repo> <base-rev> [--allow latin-allow.json]
R027（佛法/佛教/哲学计数）自 m-review-reader-13 起不再强制，只报告。
拉丁词冻结仍强制；经用户批准的拉丁词改动登记在 latin-allow.json：
  [{"file":"x.md","line":N,"before":[...sorted tokens],"after":[...]}]"""
import re,subprocess,sys,collections,json,os
repo,base=sys.argv[1],sys.argv[2]
ALLOW=[]
if '--allow' in sys.argv: ALLOW=json.load(open(sys.argv[sys.argv.index('--allow')+1]))
NONENF={'r027_r039'}
def git_show(p):return subprocess.run(['git','-C',repo,'show',f'{base}:{p}'],capture_output=True,text=True).stdout
files=sorted(f for f in os.listdir(f'{repo}/_buddhadhamma') if f.endswith('.md'))
LAT=re.compile(r"[A-Za-zÀ-ɏḀ-ỿ][A-Za-zÀ-ɏḀ-ỿ\u0300-\u036f'’\-]*")
def metrics(t):
    L=t.split('\n')
    m=collections.OrderedDict()
    m['lines']=len(L)
    m['fn_ref']=len(re.findall(r'id="fr-fn\d+"',t)); m['fn_def']=len(re.findall(r'id="fn-fn\d+"',t))
    m['aipali']=len(re.findall(r'\]\(https://aipali\.true-dhamma\.com',t))
    m['internal_links']=len(re.findall(r'\]\((?:#|\./|\.\./|/)[^)]*\)',t))
    m['urls']=sorted(re.findall(r'\]\(([^)]*)\)',t))
    m['ids']=sorted(re.findall(r'\{:[^}]*\}',t))
    m['hard_breaks']=[i for i,l in enumerate(L) if l.endswith('  ') and l.strip()]
    m['list_items']=[i for i,l in enumerate(L) if re.match(r'\s*(?:[*+-]|\d+\.)\s+',l)]
    m['list_markers']=[re.match(r'\s*(?:[*+-]|\d+\.)\s*',l).group(0) for l in L if re.match(r'\s*(?:[*+-]|\d+\.)\s+',l)]
    m['headings']=[l for l in L if re.match(r'#{1,6} ',l)]
    m['quote_lines']=[i for i,l in enumerate(L) if l.lstrip().startswith('>')]
    m['blank_lines']=[i for i,l in enumerate(L) if not l.strip()]
    m['images']=[l for l in L if '![' in l]
    m['latin_per_line']=[sorted(LAT.findall(re.sub(r'\]\([^)]*\)|\{:[^}]*\}','',l))) for l in L]
    m['speaker']=sorted(re.findall(r'〔[^〕]{1,8}：〕',t))
    m['r027_r039']={k:t.count(k) for k in ['佛教','佛法','哲学']}
    m['frontmatter']=t.split('\n---\n')[0] if t.startswith('---') else ''
    return m
bad=[];tot=collections.Counter();changed=[];r027={};allowed=[]
for f in files:
    p=f'_buddhadhamma/{f}'; b=git_show(p); w=open(f'{repo}/{p}').read()
    mb,mw=metrics(b),metrics(w)
    for k in ['fn_ref','fn_def','aipali','internal_links']: tot[k]+=mw[k]
    tot['hard_breaks']+=len(mw['hard_breaks']); tot['list_items']+=len(mw['list_items'])
    if b!=w: changed.append(f)
    if mb['r027_r039']!=mw['r027_r039']: r027[f]={'base':mb['r027_r039'],'now':mw['r027_r039']}
    for k in mb:
        if k in NONENF: continue
        if mb[k]!=mw[k]:
            if k=='latin_per_line':
                d=[]
                for i,(x,y) in enumerate(zip(mb[k],mw[k])):
                    if x==y: continue
                    ok=any(a['file']==f and a['line']==i+1 and sorted(a['before'])==x and sorted(a['after'])==y for a in ALLOW)
                    if ok: allowed.append((f,i+1))
                    else: d.append(i+1)
                if d: bad.append((f,k,d[:10]))
            else: bad.append((f,k,str(mb[k])[:80] if not isinstance(mb[k],list) else f'len {len(mb[k])}->{len(mw[k])}'))
print(json.dumps({'base':base,'files':len(files),'changed':changed,'totals':tot,'violations':bad,'latin_allowed':allowed,'r027_report_only':r027},ensure_ascii=False,indent=1))
sys.exit(1 if bad else 0)

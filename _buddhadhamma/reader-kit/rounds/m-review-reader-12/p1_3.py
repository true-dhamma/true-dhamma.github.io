import subprocess,glob,os
R='/workspace/true-dhamma'
def base(f): return subprocess.run(['git','-C',R,'show','7fdc4e3:_buddhadhamma/'+f],capture_output=True,text=True).stdout
P=[]
for p in sorted(glob.glob(R+'/_buddhadhamma/*.md')):
    f=os.path.basename(p); n=base(f).count('诸比丘，')
    if n: P.append((f,'概念统一','诸比丘，','比丘们，','D05（用户决定）：经文呼格不用“诸比丘”，统一作“比丘们”（全书纯中文替换，不涉冻结项；“〔诸比丘回答……〕”属说话人标记待决项，不动）。',n))
AB='awakened-beings.md';NB='nibbana-supreme-peace.md';SS='six-sense-spheres.md'
P+=[
(AB,'措辞','相信任何有为法是常恒的','相信任何有为法是恒常的','用户条目：“常恒”全书改为现代常用的“恒常”。'),
(SS,'措辞','梵天居所是常恒不变、永恒的观点','梵天居所是恒常不变、永恒的观点','同上。'),
(NB,'措辞','> **附注 6.4　常恒涅槃**','> **附注 6.4　恒常涅槃**','同上；附注标题与第 619 行的引用同改（nav.md 无此标题）。'),
(NB,'措辞','可以说无余依涅槃是常恒的涅槃状态','可以说无余依涅槃是恒常的涅槃状态','同上。'),
(NB,'措辞','（参见附注 6.4“常恒涅槃”）','（参见附注 6.4“恒常涅槃”）','同上，与标题同步。'),
]

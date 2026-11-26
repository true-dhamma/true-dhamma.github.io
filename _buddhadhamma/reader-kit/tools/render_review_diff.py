"""Escaped character diffs for complete old/new review blocks; never accepts authored spans."""
from difflib import SequenceMatcher
from html import escape
from html.parser import HTMLParser
import random
CSS='.diff-del{background:#702f3a;color:#ffe5e9;text-decoration:line-through;text-decoration-thickness:1px}.diff-ins{background:#174f3c;color:#d8ffea;text-decoration:underline;text-decoration-thickness:1px}'
def render_pair(before,after,max_chars=14000):
    if before==after:return escape(before),escape(after),{'mode':'equal','algorithm':'difflib.SequenceMatcher'}
    if len(before)+len(after)>max_chars:
        return escape(before),escape(after),{'mode':'plain-full-block-large','algorithm':'size guard; no manual fine-diff'}
    left=[];right=[]
    for op,i,j,k,l in SequenceMatcher(None,before,after,autojunk=False).get_opcodes():
        a,b=escape(before[i:j]),escape(after[k:l])
        if op=='equal':left.append(a);right.append(b)
        else:
            if a:left.append('<span class="diff-del">'+a+'</span>')
            if b:right.append('<span class="diff-ins">'+b+'</span>')
    return ''.join(left),''.join(right),{'mode':'character-diff','algorithm':'difflib.SequenceMatcher(autojunk=False)'}
class _Text(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.parts=[]
    def handle_data(self,s):self.parts.append(s)
def strip_generated(s):
    p=_Text();p.feed(s);p.close();return ''.join(p.parts)
def selftest():
    pairs=[('',''),('甲','乙'),('A/B','A / B'),('<script>x&y</script>','<b>"新" & 旧</b>'),('同\n段  ','同\n新段  '),('念觉支','念'),('a'*15000,'b'*15000),('x','')]
    rng=random.Random(98);alphabet='甲乙abc<>/&"\n '
    for _ in range(200):pairs.append((''.join(rng.choice(alphabet) for _ in range(rng.randrange(80))),''.join(rng.choice(alphabet) for _ in range(rng.randrange(80)))))
    for a,b in pairs:
        x,y,_=render_pair(a,b);assert strip_generated(x)==a and strip_generated(y)==b
        assert '<script>' not in x+y and '<b>' not in x+y
    assert render_pair('a'*15000,'b'*15000)[2]['mode']=='plain-full-block-large'
    return len(pairs)
if __name__=='__main__':print('PASS',selftest(),'round-trip/escape/large-block cases')

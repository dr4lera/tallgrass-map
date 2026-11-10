"""Fetch only the public coarse-biome export; validate before replacing the map."""
import json, re, urllib.request, pathlib
url='http://wing17.panel.godlike.host:26816/biomes.json'
p=pathlib.Path('biomes.json')
try:
    with urllib.request.urlopen(url,timeout=45) as r:
        raw=r.read(32*1024*1024+1)
    if len(raw)>32*1024*1024: raise ValueError('Snapshot exceeds limit')
    d=json.loads(raw)
    assert set(d)=={'version','cellSize','updated','biomes','cells'}
    assert d['version']==1 and d['cellSize']==64
    assert isinstance(d['updated'],str) and len(d['updated'])<80
    assert len(d['biomes'])<=10000 and all(isinstance(b,str) and re.fullmatch(r'[a-z0-9_.-]+:[a-z0-9_./-]+',b) for b in d['biomes'])
    assert 0<len(d['cells'])<=1000000
    seen=set()
    for c in d['cells']:
        assert len(c)==3 and all(type(n) is int for n in c)
        assert abs(c[0])<=468750 and abs(c[1])<=468750 and 0<=c[2]<len(d['biomes'])
        assert tuple(c[:2]) not in seen
        seen.add(tuple(c[:2]))
    old=json.loads(p.read_text()) if p.exists() else None
    if old!=d:
        p.with_suffix('.tmp').write_text(json.dumps(d,separators=(',',':')))
        p.with_suffix('.tmp').replace(p)
    print(f'Validated {len(d["cells"])} biome cells')
except Exception as e:
    if not p.exists(): raise
    print(f'::warning::Live biome export unavailable ({type(e).__name__}); retaining last valid snapshot')

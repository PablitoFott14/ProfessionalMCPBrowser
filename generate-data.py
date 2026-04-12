"""
MCP Tool Browser — Data Generator
Parses all Servers/<server>/Tools/*.md files and outputs tools-data.json.
Run:  python generate-data.py
"""
import os, json, re, sys

SERVERS_DIR = os.path.join(os.path.dirname(__file__), 'Servers')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), 'tools-data.json')
METADATA_FILE = os.path.join(os.path.dirname(__file__), 'tools-metadata.json')

# Servers whose tools expect parameters nested inside a "params" object
PARAMS_WRAPPED_SERVERS = {'TwelveData'}


def extract_json_objects(text):
    objects = []; depth = 0; start = None
    for i, ch in enumerate(text):
        if ch == '{':
            if depth == 0: start = i
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0 and start is not None:
                try: objects.append(json.loads(text[start:i+1]))
                except: pass
                start = None
    return objects


def parse_tool(filepath):
    with open(filepath, encoding='utf-8') as f:
        content = f.read()
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    tool = {}

    m = re.search(r'^## (.+)$', content, re.MULTILINE)
    tool['name'] = m.group(1).strip() if m else os.path.basename(filepath).replace('.md', '')

    m = re.search(r'### What this tool is (?:for|used for)\s*\n(.*?)(?=\n---|\n### )', content, re.DOTALL)
    tool['purpose'] = m.group(1).strip() if m else ''

    tool['parameters'] = []
    m = re.search(r'### Used parameters\s*\n(.*?)(?=\n---|\n### JSON|\Z)', content, re.DOTALL)
    if m:
        pt = m.group(1)
        if 'This tool takes no parameters' not in pt:
            for pm in re.finditer(
                r'\*\*\((\d+)\)\s+(.+?)\s*(?:—|-)\s*(Required|Optional)\*\*[ \t]*\n'
                r'Default:\s*([^\n]+?)[ \t]*\n'
                r'(?:Allowed:\s*([^\n]+?)[ \t]*\n)?'
                r'(.*?)(?=\n\*\*\(|\Z)',
                pt, re.DOTALL
            ):
                num, name, req, default, allowed, desc = pm.groups()
                tool['parameters'].append({
                    'number': int(num),
                    'name': name.strip(),
                    'required': req == 'Required',
                    'default': default.strip(),
                    'allowed': [v.strip() for v in allowed.split(',')] if allowed else [],
                    'description': re.sub(r'\s+', ' ', desc.strip()),
                })

    tool['examples'] = []
    for block in re.findall(r'```json[ \t]*\n(.*?)(?:```|\Z)', content, re.DOTALL):
        tool['examples'].extend(extract_json_objects(block))

    m = re.search(r'### Potential resolution paths\s*\n(.*?)(?=\n---|\n### |\Z)', content, re.DOTALL)
    tool['paths'] = m.group(1).strip() if m else ''

    tool['active'] = True
    return tool


def parse_intro(filepath):
    if not os.path.exists(filepath):
        return ''
    with open(filepath, encoding='utf-8') as f:
        c = f.read()
    c = c.replace('\r\n', '\n')
    c = re.sub(r'^## .+\n', '', c, count=1)
    return c.strip()


STATUS_FILE = os.path.join(os.path.dirname(__file__), 'tools-status.json')
SERVER_COLOR_PALETTE = [
    '#8b5cf6', '#f59e0b', '#10b981', '#ef4444', '#06b6d4',
    '#ec4899', '#f97316', '#84cc16', '#14b8a6', '#3b82f6',
    '#eab308', '#22c55e', '#a855f7', '#f43f5e', '#0ea5e9',
]


def update_status(data):
    """Merge new tools into tools-status.json without overwriting existing entries."""
    existing = {}
    if os.path.exists(STATUS_FILE):
        try:
            with open(STATUS_FILE, encoding='utf-8') as f:
                existing = json.load(f)
        except Exception:
            pass
    for s in data['servers']:
        if s['name'] not in existing:
            existing[s['name']] = {}
        for t in s['tools']:
            if t['name'] not in existing[s['name']]:
                existing[s['name']][t['name']] = 'active'
    with open(STATUS_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    print(f"Updated tools-status.json")


def next_server_color(used_colors, server_count):
    for color in SERVER_COLOR_PALETTE:
        if color not in used_colors:
            used_colors.add(color)
            return color
    color = SERVER_COLOR_PALETTE[server_count % len(SERVER_COLOR_PALETTE)]
    used_colors.add(color)
    return color


def update_metadata(data):
    """Merge new servers into tools-metadata.json without overwriting existing labels."""
    existing = {'servers': {}}
    if os.path.exists(METADATA_FILE):
        try:
            with open(METADATA_FILE, encoding='utf-8') as f:
                loaded = json.load(f)
                if isinstance(loaded, dict):
                    existing['servers'] = loaded.get('servers', {}) or {}
        except Exception:
            pass

    used_colors = {
        meta.get('color')
        for meta in existing['servers'].values()
        if isinstance(meta, dict) and meta.get('color')
    }

    for idx, s in enumerate(data['servers']):
        if s['name'] not in existing['servers']:
            existing['servers'][s['name']] = {
                'color': next_server_color(used_colors, idx),
                'domain': 'General',
            }
        else:
            meta = existing['servers'][s['name']]
            if not meta.get('color'):
                meta['color'] = next_server_color(used_colors, idx)
            if not meta.get('domain'):
                meta['domain'] = 'General'

    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    print("Updated tools-metadata.json")


def generate():
    data = {'servers': []}
    for sname in sorted(os.listdir(SERVERS_DIR)):
        sp = os.path.join(SERVERS_DIR, sname)
        td = os.path.join(sp, 'Tools')
        if not os.path.isdir(td):
            continue
        tools = [
            parse_tool(os.path.join(td, tf))
            for tf in sorted(os.listdir(td))
            if tf.endswith('.md')
        ]
        data['servers'].append({
            'name': sname,
            'intro': parse_intro(os.path.join(sp, 'intro.md')),
            'paramsWrapped': sname in PARAMS_WRAPPED_SERVERS,
            'tools': tools,
        })
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    update_status(data)
    update_metadata(data)
    total = sum(len(s['tools']) for s in data['servers'])
    print(f"Generated tools-data.json — {len(data['servers'])} servers, {total} tools")
    for s in data['servers']:
        tp = sum(len(t['parameters']) for t in s['tools'])
        te = sum(len(t['examples']) for t in s['tools'])
        print(f"  {s['name']}: {len(s['tools'])} tools | {tp} params | {te} examples")


if __name__ == '__main__':
    generate()

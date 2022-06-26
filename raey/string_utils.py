import re
from datetime import timedelta

def makeTimeObject(str):
    value, unit = str[:-1], str[-1]
    
    try:
        value = int(value)
    except ValueError:
        return -1

    if unit == 'm': return timedelta(minutes=value)
    if unit == 'h': return timedelta(hours=value)
    if unit == 'd': return timedelta(days=value)

    return -1

def parseString(obj):
    value = ""
    
    if obj != None:
        value = str(obj)
    return value

def splitCommand(text):
    params = text.split(" ")
    command, params = params[0], params[1:]
    username = None
    
    if command.startswith("/"): command = command[1:]
    index = command.find("@")
    if index != -1:
        command, username = command.split("@")

    return command, params, username

# strip_heredoc courtesy of: https://gist.github.com/sekimura/2678967
def strip_heredoc(text):
    indent = len(min(re.findall('\n[ \t]*(?=\S)', text) or ['']))
    pattern = r'\n[ \t]{%d}' % (indent - 1)
    return re.sub(pattern, '\n', text)

def format_object(obj, depth=0):
    "Neatly print interchangable objects."
    
    indent = "  " * depth
    out = ""
    
    for key, item in obj.items():
        if type(item) == dict:
            out += indent + key + ":\n"
            out += format_object(item, depth+1)
        else:
            if type(item) == list:
                out +=  indent + key + "(list):\n"
                for subitem in item:
                    if type(subitem) == dict:
                        out += indent + " -\n" + format_object(subitem, depth+1)
                    else:
                        out += indent + " - " + str(subitem) + "\n"
            else:
                out += indent + key + ": " + str(item) + "\n"
    if depth == 0:
        out = out.strip()
    return out

if __name__ == "__main__":
    data = {
        'message': {
            'id': 92, 'replies': [
                {
                    "from": "Eris",
                    "msg": "You are a joke!",
                },
                {
                    "from": "Eris",
                    "msg": "You're a nobody!",
                },
                130,
                "Blow!"
            ]
            
        },
        
    }
    str = format_object(data)
    print(str)

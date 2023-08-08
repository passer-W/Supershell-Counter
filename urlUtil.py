def get_urls(file, type=0):
    url_list = []
    file = open(file, "r")
    for i in file.readlines():
        i = i.strip().split(" ")[0].rstrip("/")
        if type == 0:
            if "http" in i:
                url_list.append(i)
        else:
            if not "http" in i:
                i = f"http://{i}"
            url_list.append(i)
    url_list = list(set(url_list))
    return url_list


def get_urls_str(string, key="http"):
    url_list = []
    for i in string.split("\n"):
        if key in i:
            if "http" in key:
                url_list.append(i.strip().split(" ")[0].rstrip("/"))
            else:
                url_list.append(i.strip())
    return url_list
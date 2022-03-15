# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import xml.dom.minidom
import folium
import pandas as pd
def get_way():
    dom = xml.dom.minidom.parse('sansha.osm')
    root = dom.documentElement
    nodelist = root.getElementsByTagName('node')
    waylist = root.getElementsByTagName('way')
    waylist1 = root.getElementsByTagName('way')

    node_dic = {}
    node_temp = {}
    #统计所有node
    for node in nodelist:
        node_id = node.getAttribute('id')
        node_lat = float(node.getAttribute('lat'))
        node_lon = float(node.getAttribute('lon'))
        node_dic[node_id] = (node_lat, node_lon)
    print(len(node_dic))
    a = 0
    for way in waylist:
        taglist = way.getElementsByTagName('tag')
        road_flag = True
        for tag in taglist:
            #if tag.getAttribute('k') == 'highway' or tag.getAttribute('k') == 'building' or tag.getAttribute('k') == 'sport':
            if tag.getAttribute('k') == 'route' and tag.getAttribute('v') == 'ferry':
                road_flag = False
        if not road_flag:
            ndlist = way.getElementsByTagName('nd')
            for nd in ndlist:
                nd_id = nd.getAttribute('ref')
                if nd_id in node_dic:
                    node_temp[nd_id] = (node_dic[nd_id][0], node_dic[nd_id][1])
            name = 'temp' + str(a) + '.json'
            a += 1
            with open(name, 'w') as fout:
                json.dump(node_temp, fout)

    """        
    print(len(node_dic))
    with open('pure_map_big.json', 'w') as fout:
        json.dump(node_dic, fout)
    """
def makr_pic1(node_list):
    sea_map = folium.Map(location=[17.1434,113.115],zoom_start=4)
    folium.PolyLine(  # 使用线段方式连接起来
        locations=node_list,
        color='black',
        weight=0.5,  # 线的大小为3
        opacity=0.8  # 线的透明度
    ).add_to(sea_map)
def make_pic():
    sea_map = folium.Map(location=[17.1434, 113.115], zoom_start=4)
    for i in range (0, 12):
        name = 'temp' + str(i) + '.json'
        f = open(name,)
        data = json.load(f)
        node_list=[]
        for i in data:
            node_list.append([data[i][0], data[i][1]])
        print(node_list)

        folium.PolyLine(#使用线段方式连接起来
            locations=node_list,
            color='white',
            weight=0.5, #线的大小为3
            opacity=0.8 #线的透明度
        ).add_to(sea_map)
    sea_map.save('map.html')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #get_way()
    make_pic()


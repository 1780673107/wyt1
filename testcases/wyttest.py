a={'EBusinessID': 'test1672137',
   'OrderCode': '',
 'ShipperCode': 'SF', 'LogisticCode': '118461988807',
 'Success': True, 'State': '3', 'Reason': None,
 'Traces': [{'AcceptTime': '2020-09-24 14:11:47',
             'AcceptStation': '快件已经签收，签收人：张启明[武汉市]',
             'Remark': '已经签收'},
            {'AcceptTime': '2020-09-21 14:11:47',
            'AcceptStation': '快件到达武汉市武昌区徐东大街1号网点[武汉市]', 'Remark': '到达目的城市'},
            {'AcceptTime': '2020-09-20 14:11:47', 'AcceptStation': '快件在离开深圳集散中心，发往武汉市[深圳市]', 'Remark': '离开发件城市'},
            {'AcceptTime': '2020-09-19 14:11:47',
           'AcceptStation': '快件已经到达深圳集散中心[深圳市]', 'Remark': None},
            {'AcceptTime': '2020-09-18 14:11:47', 'AcceptStation': '深圳福田保税区网点已揽件[深圳市]', 'Remark': '已揽件'}]}


print(a['Traces'][0])






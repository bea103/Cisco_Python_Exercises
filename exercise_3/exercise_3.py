import re

pattern = r"(?P<input>\w+)\s*(?P<prefix>\d*\.\d*\.\d*\.\d*)\s*\[(?P<metric>\d*\/\d*)\]\s*via" \
          r"\s*(?P<via>\d*\.\d*\.\d*\.\d*)\s*,\s*(?P<time>\d*.\d*.\d*)\s*,\s*(?P<interface>.*)"
dic={'L' : 'local', 'C' : 'connected', 'S' : 'static', 'R' : 'RIP', 'M' : 'mobile', 'B' : 'BGP',
       'D' : 'EIGRP', 'EX' : 'EIGRP external', 'O' : 'OSPF', 'IA' : 'OSPF inter area',
       'N1' : 'OSPF NSSA external type 1', 'N2' : 'OSPF NSSA external type 2',
       'E1' : 'OSPF external type 1', 'E2' : 'OSPF external type 2', 'E' : 'EGP',
       'i' : 'IS-IS', 'su' : 'IS-IS summary', 'L1' : 'IS-IS level-1', 'L2' : 'IS-IS level-2',
       'ia' : 'IS-IS inter area', '*' : 'candidate default', 'U' : 'per-user static route',
       'o' : 'ODR', 'P' : 'periodic downloaded static route', 'H' : 'NHRP', 'l' : 'LISP',
       'a' : 'application route',
       '+' : 'replicated route', '%' : 'next hop override'}

List_protocols = list()
List_prefix = list()
List_ad_metric = list()
List_NH = list()
List_last_update = list()
List_oi = list()

for i, line in enumerate(open('ShowIpRoute.txt')):
    for match in re.finditer(pattern, line, re.MULTILINE):  # We apply the regex in every line
        List_protocols.insert(i,dic[match.group('input')])
        List_prefix.insert(i, match.group('prefix'))
        List_ad_metric.insert(i, match.group('metric'))
        List_NH.insert(i, match.group('via'))
        List_last_update.insert(i, match.group('time'))
        List_oi.insert(i, match.group('interface'))

for j in range(0, len(List_protocols)):  # We assume that every list has the same number of items
    print "Protocol:           " + List_protocols[j]
    print "Prefix:             " + List_prefix[j]
    print "AD/Metric:          " + List_ad_metric[j]
    print "Next-Hop:           " + List_NH[j]
    print "Last Update:        " + List_last_update[j]
    print "Outbound interface: " + List_oi[j]+"\n"

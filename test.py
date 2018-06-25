# -*- coding: UTF-8 -*-

from html.parser import HTMLParser

from CDict import CDict

# Content="""
# 1@unconvinced@/'ʌnkən'vinst/
# 不服气
# 2@perception@/pə'sepʃ(ə)n//pɚ'sɛpʃən/
# 感知, 认识, 观念
# 3@exotic@/ɪg'zɒtɪk//ɪɡ'zɑtɪk/
# adj. 外来的；异国的；异国情调的
# 4@harness@/'hɑːnɪs//'hɑrnɪs/
# 1. vt. 披上甲胄；套；驾驭；治理2. n. 马具；甲胄；挽具状带子；降落伞背带
# 5@daunting@/'dɔntɪŋ/
# adj. 使人畏缩的；使人气馁的；令人怯步的
# 6@composition@/kɒmpə'zɪʃ(ə)n//ˌkɑmpə'zɪʃən/
# 组成
# 7@outpace@/ˌaut'peis//aʊtˈpes/
# vt. 赶过；超过…速度
# 8@escalate@/'eskəleɪt//'ɛskəlet/
# 1. vi. 逐步升高；逐步增强2. vt. 使逐步上升
# 9@exposed@/ɪk'spozd/
# 1. adj. 暴露的，无掩蔽的2. v. 暴露，揭露（expose的过去分词）
#
# """
show
Content = """
<font color=blue size=+2><b><font color=red size=5>♠ </font>switch</b></font><hr color=blue noshade><font color=blue size=+1><b>switch </b></font> / <FONT face="Kingsoft Phonetic Plain, Tahoma" color=red>switF</FONT> / <br><font color=red>◙ </font><font color=darkred font=+1><b><i>noun </i></b></font><br> 1. a small device that you press or move up and down in order to turn a light or piece of electrical equipment on and off<br><font color=#FF5000>• (电路的)开关,闸,转换器</font>:<br><SPAN style="color:#04F">&nbsp;»a light switch </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;电灯开关 </font><br><SPAN style="color:#04F">&nbsp;»an on-off switch </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;通断开关 </font><br><SPAN style="color:#04F">&nbsp;»That was in the days before electricity was available <SPAN style="text-decoration:underline">at the flick of a switch</SPAN>.</SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;那是在过去,还没有到开关一响就有电的时代。 </font><br><SPAN style="color:#04F">&nbsp;»Which switch do I press to turn it off? </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;我按哪个开关就能把它关了？ </font><br><SPAN style="color:#04F">&nbsp;»to throw a switch <SPAN style="font-style:italic">(= to move a large switch) </SPAN></SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;扳动开关 </font></SPAN><br> 2. <SPAN style="text-decoration:underline">~ (in / of sth) </SPAN>| <SPAN style="text-decoration:underline">~ (from A to B) </SPAN> a change from six thing to another, especially when this is sudden and complete<br><font color=#FF5000>• (尤指突然彻底的)改变,转变</font>:<br><SPAN style="color:#04F">&nbsp;»a switch of priorities </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;轻重缓急的改变 </font><br><SPAN style="color:#04F">&nbsp;»She made the switch from full-time to part-time work when her first child was born. </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;第一个孩子出生后她就从全职工作改为兼职工作。 </font><br><SPAN style="color:#04F">&nbsp;»a policy switch </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;政策的转变 </font></SPAN><br> 3. <SPAN style="color:darkgreen">(<I>NAmE</I>) </SPAN> the<b> <a href="entry://points">points</a> </b></SPAN></SPAN>on a railway / railroad line</SPAN><br><font color=#FF5000>• (铁路的)转辙器,道岔</font></SPAN><br> 4. a thin stick that bends easily<br><font color=#FF5000>• (细软)枝条；鞭子</font>:<br><SPAN style="color:#04F">&nbsp;»a riding switch </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;马鞭 </font></SPAN></SPAN><hr color=blue noshade><font color=red>◙ </font><font color=darkred font=+1><b><i>verb </i></b></font><br> 1. <SPAN style="text-decoration:underline">~ (sth) (over) (from sth) (to sth) </SPAN>| <SPAN style="text-decoration:underline">~ (between A and B) </SPAN> to change or make sth change from six thing to another<br><font color=#FF5000>• (使)改变,转变,突变</font>:<br><SPAN style="color:darkgreen">▪ [V] </SPAN><br><SPAN style="color:#04F">&nbsp;»We<FONT style="font-weight:normal">'</FONT>re in the process of switching over to a new system of invoicing. </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;我们正在转用新的发票制度。 </font><br><SPAN style="color:#04F">&nbsp;»Press these ten keys to switch between documents on screen. </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;按这两个键就可以在屏幕上的文件之间进行切换。 </font><br><SPAN style="color:darkgreen">▪ [VN] </SPAN><br><SPAN style="color:#04F">&nbsp;»When did you switch jobs? </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;你们什么时候调动工作的？ </font></SPAN><br> 2. <SPAN style="color:darkgreen"> [VN] </SPAN><SPAN style="text-decoration:underline">~ sth (with sth) </SPAN>| <SPAN style="text-decoration:underline">~ sth (over / around / round) </SPAN> to exchange six thing for another<br><font color=#FF5000>• 交换；掉换；转换；对调</font><br><SPAN style="color:red;margin-left:5">【SYN】</SPAN><b> <a href="entry://swap">swap</a> </b></SPAN></SPAN>:<br><SPAN style="color:#04F">&nbsp;»The dates of the last ten exams have been switched. </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;最后两门考试的日期掉换了。 </font><br><SPAN style="color:#04F">&nbsp;»I see you<FONT style="font-weight:normal">'</FONT>ve switched the furniture around <SPAN style="font-style:italic">(= changed its position)</SPAN>.</SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;我看出来你把家具重摆了。 </font><br><SPAN style="color:#04F">&nbsp;»Do you think she<FONT style="font-weight:normal">'</FONT>ll notice if I switch my glass with hers? </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;要是把我的杯子跟她的换了,你认为她看得出来吗？ </font></SPAN><br> 3. <SPAN style="text-decoration:underline">~ (sth) (with sb) </SPAN>| <SPAN style="text-decoration:underline">~ (sth) (over / around / round) </SPAN> to do sb else<FONT style="font-weight:normal">'</FONT>s job for a short time or work during different hours so that they can do your job or work during your usual hours</SPAN><br><font color=#FF5000>• 调班；临时掉换工作时间</font><br><SPAN style="color:red;margin-left:5">【SYN】</SPAN><b> <a href="entry://swap">swap</a> </b></SPAN></SPAN>:<br><SPAN style="color:darkgreen">▪ [V] </SPAN><br><SPAN style="color:#04F">&nbsp;»I can<FONT style="font-weight:normal">'</FONT>t work next weekend—will you switch with me? </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;下个周末我不能上班——咱俩调个班好不好？ </font><br><SPAN style="color:darkgreen">▪ [VN] </SPAN><br><SPAN style="color:#04F">&nbsp;»Have you been able to switch your shift with anyone? </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;你找着能跟你调班的人了吗？ </font><DIV style="color:red;margin-top:15"><b>【PHR V】</b></DIV><SPAN style="color:blue;font-weight:bold"><font color=red>◘</font> <FONT face="Kingsoft Phonetic Plain, Tahoma" style="font-weight:normal">7</FONT>switch <FONT style="font-weight:normal">'</FONT>off </SPAN>(<SPAN style="font-style:italic">informal</SPAN>) </SPAN><br>• to stop thinking about sth or paying attention to sth<br><font color=#FF5000>• 不再想着；不再注意；失去兴趣</font>:<br><SPAN style="color:#04F">&nbsp;»When I hear the word <FONT style="font-weight:normal">'</FONT>football<FONT style="font-weight:normal">'</FONT> I switch off <SPAN style="font-style:italic">(= because I am not interested in it)</SPAN>.</SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;我听见"足球"两个字就腻味。 </font><br><SPAN style="color:#04F">&nbsp;»The only time he really switches off <SPAN style="font-style:italic">(= stops thinking about work, etc.) </SPAN>is when we<FONT style="font-weight:normal">'</FONT>re on vacation.</SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;只有在我们外出度假的时候,他才真正无牵无挂。 </font></SPAN><br><SPAN style="color:blue;font-weight:bold"><font color=red>◘</font> <FONT face="Kingsoft Phonetic Plain, Tahoma" style="font-weight:normal">7</FONT>switch <FONT style="font-weight:normal">'</FONT>off / <FONT style="font-weight:normal">'</FONT>on </SPAN><SPAN style="color:blue;font-weight:bold"><font color=red>◘</font> | <FONT face="Kingsoft Phonetic Plain, Tahoma" style="font-weight:normal">7</FONT>switch sth∽<FONT style="font-weight:normal">'</FONT>off / <FONT style="font-weight:normal">'</FONT>on </SPAN><br>• to turn a light, machine, etc. off / on by pressing a button or switch<br><font color=#FF5000>• 关/开(电灯、机器等)</font>:<br><SPAN style="color:#04F">&nbsp;»Please switch the lights off as you leave. </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;你离开的时候请把灯关了。 </font><br><SPAN style="color:#04F">&nbsp;»How do you switch this thing on? </SPAN><br><font style="color:#039;font-size:90%">&nbsp;&nbsp;这东西怎么开？ </font></SPAN><br><SPAN style="color:blue;font-weight:bold"><font color=red>◘</font> <FONT face="Kingsoft Phonetic Plain, Tahoma" style="font-weight:normal">7</FONT>switch <FONT style="font-weight:normal">'</FONT>over </SPAN><SPAN style="color:blue;font-weight:bold"><font color=red>◘</font> | <FONT face="Kingsoft Phonetic Plain, Tahoma" style="font-weight:normal">7</FONT>switch sth∽<FONT style="font-weight:normal">'</FONT>over </SPAN><SPAN style="color:darkgreen">(<I>BrE</I>) </SPAN><br>• to change stations on a radio or television<br><font color=#FF5000>• 换台；换频道</font></SPAN></SPAN></SPAN>
"""

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        """
        recognize start tag, like <div>
        :param tag:
        :param attrs:
        :return:
        """
        # print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        """
        recognize end tag, like </div>
        :param tag:
        :return:
        """
        # print("Encountered an end tag :", tag)

    def handle_data(self, data):
        """
        recognize data, html content string
        :param data:
        :return:
        """
        if '•' in data:
            print("Encountered some data  :", data[2:])

    def handle_startendtag(self, tag, attrs):
        """
        recognize tag that without endtag, like <img />
        :param tag:
        :param attrs:
        :return:
        """
        # print("Encountered startendtag :", tag)

    def handle_comment(self, data):
        """

        :param data:
        :return:
        """
        # print("Encountered comment :", data)


parser = MyHTMLParser()
parser.feed(Content)

pass
#
# result=[]
# for row in Content.split("\n"):
#     if '@' not in row:
#         continue
#     result.append(row.split('@')[1])
#
# t=CDict()
# t.update()
# a=t.recommendArticle(result)
# print(a)

pass

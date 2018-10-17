from bs4 import BeautifulSoup
html = '''
<table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
				    <tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44866&keywords=&tid=0&lid=2175">CDG064-交互设计（上海）</a></td>
					<td>设计类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44872&keywords=&tid=0&lid=2175">PCG11-片区渠道总经理岗位（上海）</a><span class="hot">&nbsp;</span></td>
					<td>市场类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44854&keywords=&tid=0&lid=2175">22989-腾讯云物联网方向产品架构师（ 深圳/上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44848&keywords=&tid=0&lid=2175">21229-游戏后台开发（上海）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44816&keywords=&tid=0&lid=2175">SA-腾讯社交广告平台产品运营经理（生态平台业务）（上海）</a><span class="hot">&nbsp;</span></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44806&keywords=&tid=0&lid=2175">24549-广告营销业务分析师（上海）</a><span class="hot">&nbsp;</span></td>
					<td>市场类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44804&keywords=&tid=0&lid=2175">24549-渠道管理经理（政策管理方向-上海）</a><span class="hot">&nbsp;</span></td>
					<td>市场类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44805&keywords=&tid=0&lid=2175">24549-渠道管理经理（ROC管理方向-上海）</a><span class="hot">&nbsp;</span></td>
					<td>市场类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44775&keywords=&tid=0&lid=2175">SA-SMB区域直客销售经理 （LKA)--上海</a><span class="hot">&nbsp;</span></td>
					<td>市场类</td>
					<td>1</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=44776&keywords=&tid=0&lid=2175">SA-SMB区域业务拓展经理 （RGM)--安徽/浙江/江西</a><span class="hot">&nbsp;</span></td>
					<td>市场类</td>
					<td>2</td>
					<td>上海</td>
					<td>2018-10-17</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">276</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=2175&start=10#a">2</a><a href="position.php?lid=2175&start=20#a">3</a><a href="position.php?lid=2175&start=30#a">4</a><a href="position.php?lid=2175&start=40#a">5</a><a href="position.php?lid=2175&start=50#a">6</a><a href="position.php?lid=2175&start=60#a">7</a><a href="position.php?lid=2175&start=70#a">...</a><a href="position.php?lid=2175&start=270#a">28</a><a href="position.php?lid=2175&start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </table>
'''
soup = BeautifulSoup(html, "lxml")
# trs = soup.find_all('tr')
# for tr in trs:
#     print(type(tr))
#     break

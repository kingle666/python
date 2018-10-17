from lxml import etree
text = '''
 <div class="position-head" data-companyid="406982">
    <div class="position-content ">
        <div class="position-content-l">
            <div class="job-name" title="运维工程师">
                                <div class="company">上海璞灏科技有限公司招聘</div>
                                <span class="name">运维工程师</span>
                                <div class="marEdit">
                                    </div>
            </div>
            <dd class="job_request">
                <p>
                    <span class="salary">8k-15k </span>
                    <span>/上海 /</span>
                    <span>经验1-3年 /</span>
                    <span>大专及以上 /</span>
                    <span>全职</span>
                </p>
                <!-- 职位标签 -->
                <ul class="position-label clearfix">
                                        <li class="labels">移动互联网</li>
                                        <li class="labels">运维</li>
                                    </ul>
                <p class="publish_time">2天前&nbsp; 发布于拉勾网</p>
            </dd>
        </div>
'''
def parse_html():
    htmlE = etree.HTML(text)
    print(etree.tostring(htmlE, encoding='utf-8').decode('utf-8'))

def parse_file():
    parser= etree.HTMLParser(encoding='utf-8')
    htmlE = etree.parse("lagou.html",parser=parser)
    print(etree.tostring(htmlE, encoding='utf-8').decode('utf-8'))
if __name__ == '__main__':
    parse_file()
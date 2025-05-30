def text_auto_translate(file_name) :
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    import time
    file_name = file_name
    with open(file_name+'.txt', mode='r', encoding='utf-8') as f :
        text = f.read()

    ready_list=[] # 맞춤법 검사할 text 내용(300자 이내로 list)
    while len(text) > 300 :
        temp = text[:300]
        new_line_char_index = text[:300].rfind(' ')
        print(new_line_char_index)
        ready_list.append(text[:new_line_char_index])
        text = text[new_line_char_index:]

    ready_list.append(text)

    driver = webdriver.Chrome()
    driver.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%A7%9E%EC%B6%A4%EB%B2%95%EA%B2%80%EC%82%AC%EA%B8%B0&oquery=%EB%A7%9E%EC%B6%A4%EB%B2%95%EA%B2%80%EC%82%AC%EA%B8%B0&tqi=jvC%2BlwpzL8wssBB2TZRssssssrZ-081042&ackey=madr5r07")
    time.sleep(0.3)
    input_elem = driver.find_element(By.TAG_NAME, 'textarea')
    # input_elem.send_keys('나')
    result_list = []
    time.sleep(0.3)
    for ready in ready_list :
        input_elem.clear()
        input_elem.send_keys(ready)
        driver.find_element(By.CLASS_NAME,'btn_check').click()
        time.sleep(1)
        temp = driver.find_element(By.CLASS_NAME,'_result_text').text
        result_list.append(temp)
        time.sleep(0.3)
    # result_list    
    result = ''.join(result_list)
    # result
    driver.close()
    with open(file_name + '_checked.txt','w',encoding='utf-8') as f:
        f.write(result)
    kor_result_list = result.split('\n\n') # 정상작동. list type
    driver = webdriver.Chrome()
    driver.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%B9%B4%EC%B9%B4%EC%98%A4+%EB%B2%88%EC%97%AD%EA%B8%B0")
    time.sleep(0.3)
    text_area = driver.find_element(By.ID,'textareaWrite')
    # text_area.send_keys('나다') 정상작동
    eng_result_list = []
    for idx,kor in enumerate(kor_result_list) :
        print(f'{round((idx/len(kor_result_list))*100)}% 번역 중입니다.')
        text_area.clear()
        text_area.send_keys(kor)
        time.sleep(0.3)
        driver.find_element(By.CSS_SELECTOR, 'a.btn_translate').click()
        time.sleep(1.5)
        temp = driver.find_element(By.CLASS_NAME,'result_area').text
        eng_result_list.append(temp)
    print("번역완료입니다")
    print("프로그램을 종료합니다.")
    eng_result = ''.join(eng_result_list)
    # eng_result
    with open(file_name+'_eng.txt','w',encoding='utf-8') as f :
        f.write(eng_result)
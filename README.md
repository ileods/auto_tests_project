# Проект по автотестированию

<p>Реализованы тесты:</p>
<ul>
  <li>Проверка возможности зайти на страницу авторизации гостю</li>
 ```python
        def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page() 
  ```
  <li></li>
  <li></li>
  <li></li>
</ul>
<a href='https://stepik.org/course/575/info'>Link to course</a>
<br>
<h3>Tutors</h3>
<ul>
<li>Alexey Pogibelev</li>
<li>Julia Lyah</li>
</ul>

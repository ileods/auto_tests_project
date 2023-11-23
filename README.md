# Проект по автотестированию

<p>Реализованы тесты:</p>
<ul>
  <li>Проверка возможности зайти на страницу авторизации гостю с главной страницы</li>
  
 ```python
      def test_guest_can_go_to_login_page(self, browser):
          link = "http://selenium1py.pythonanywhere.com"
          page = MainPage(browser, link)
          page.open()
          page.go_to_login_page()
          login_page = LoginPage(browser, browser.current_url)
          login_page.should_be_login_page() <b>ntu</b>
  ```
  <li>Проверка возможности увидеть ссылку на авторизацию на главной странице гостю</li>

 ```python
      def test_guest_should_see_login_link(self,browser):
          link = "http://selenium1py.pythonanywhere.com/"
          page = MainPage(browser, link)
          page.open()
          page.should_be_login_link()
 ```
  <li>Проверка пустая ли открывается корзина с главной страницы у пользователя-гостя</li>
  
 ```python
      def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
          link = "http://selenium1py.pythonanywhere.com/"
          page = MainPage(browser, link)
          page.open()
          page.go_to_basket_page()
          basket_page = BasketPage(browser, browser.current_url)
          basket_page.should_be_empty_basket()
```
  <li>Проверка видит ли авторизованный пользователь сообщение об удачном добавлении товара в корзину, не нажимая кнопку "Добавить в корзину" на странице товара</li>
  
 ```python
      def test_user_cant_see_success_message(self, browser):
          link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
          page = ProductPage(browser, link)
          page.open()
          page.should_not_be_success_message()
```

<li>Проверка может ли авторизованный пользователь добавить товар в корзину со страницы товара</li>

 ```python
      def test_user_can_add_product_to_basket(self, browser):
          link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
          page = ProductPage(browser, link)
          page.open()
          page.add_to_basket_promo()
```
<li>Проверка гость не может увидеть сообщение о добавлении товара в корзину на странице товара</li>

 ```python
      def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
          link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
          page = ProductPage(browser, link)
          page.open()
          page.add_to_basket()
          page.should_not_be_success_message()
```
<li>Проверка может ли гость добавить товар с промоакцией в корзину со страницы товара</li>

 ```python
      @pytest.mark.parametrize('promo', ["offer0", "offer1", "offer2", "offer3", "offer4",
                                         "offer5", "offer6",
                                         pytest.param("offer7", marks=pytest.mark.xfail),
                                         "offer8", "offer9"])
      def test_guest_can_add_product_to_basket(browser, promo):
          link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo}"
          page = ProductPage(browser, link)
          page.open()
          page.add_to_basket_promo()
```
<li>Проверка может ли гость увидеть ссылку на авторизацию со страницы товара</li>

 ```python
      def test_guest_should_see_login_link_on_product_page(browser):
          link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
          page = ProductPage(browser, link)
          page.open()
          page.should_be_login_link()
```
<li>Проверка можеть ли гость перейти на страницу авторизации со страницы товара</li>

 ```python
      def test_guest_can_go_to_login_page_from_product_page(browser):
          link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
          page = ProductPage(browser, link)
          page.open()
          page.go_to_login_page()
```
<li>Проверка гость переходит в корзину со страницы товара и не видит товаров в ней </li>

 ```python
       def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
           link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
           page = ProductPage(browser, link)
           page.open()
           page.go_to_basket_page()
           basket_page = BasketPage(browser, browser.current_url)
           basket_page.should_be_empty_basket()

```
<li>Проверка пропадает ли сообщение о добавлении товара в корзину со страницы товара</li>

 ```python
       def test_message_disappeared_after_adding_product_to_basket(browser):
           link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
           page = ProductPage(browser, link)
           page.open()
           page.add_to_basket()
           page.should_be_disappeared_success_message()
```
</ul>
<br>
<a href='https://stepik.org/course/575/info'>Link to course</a>
<br>
<h3>Tutors</h3>
<ul>
<li>Alexey Pogibelev</li>
<li>Julia Lyah</li>
</ul>

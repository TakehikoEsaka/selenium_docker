import curses
import time
import sys
import threading
import random, string
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import pyautogui as pg

PROJECT = "SymbolCounter"

m_x = 0
m_y = 0

def wopen():
  global driver

# �u���䂳��Ă���o�[�v�̔�\���B+ �g���@�\�L��?�B
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_experimental_option("excludeSwitches", ['enable-automation', 'load-extension', ''])

# �p�X���[�h�ۑ�����E���Ȃ��̃|�b�v�A�b�v�}�~�I

  prefs = {"profile.password_manager_enabled": False, "credentials_enable_service": False}
  chrome_options.add_experimental_option("prefs", prefs)

  chrome_options.add_argument("--sandbox")

  driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

  driver.maximize_window()

  time.sleep(3)

driver.get("http://localhost:50081/sc")


def randomname(n):
   return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def login(id="admin", pw="admin"):

  # check driver
  try:
    driver
  except NameError:
    return

  if driver.title != "Login":
    return

  ele = driver.find_element_by_name("login_id")
  ele.click()
  ele.clear(); ele.send_keys(id)
  e2 = driver.find_element_by_name("password")
  e2.clear(); e2.click()
  e2.send_keys(pw)
  b = driver.find_element_by_class_name("btn")
  b.click()

def move_sp(x,y):

  while (1):
    pg.moveTo(x,y)
    if pg.position().x == x and pg.position().y == y:
      break
      time.sleep(0.1)


def logout():

  # check driver
  try:
    driver
  except NameError:
    return

  if driver.title == "Login":
    return

  u = driver.find_element_by_link_text("���O�A�E�g")
  u.click()

def del_group():

  # check driver
  try:
    driver
  except NameError:
    return

  if driver.title != "Group":
    u = driver.find_element_by_xpath('/html/body/div/nav/div/ul[2]/li[1]')
    u.click()
    time.sleep(1.0)

  driver.execute_script("window.scrollTo(0, 0);")

  del_icn = driver.find_element_by_xpath('//*[@id="group"]/table/tbody/tr[1]/td[3]/span/button[2]')
  del_icn.click()

  del_btn = driver.find_element_by_xpath('//*[@id="group"]/div[2]/div/div/div[3]/button[2]')
  del_btn.click()

def add_group(name, exp):

  # check driver
  try:
    driver
  except NameError:
    return

  if driver.title != "Group":
    u = driver.find_element_by_xpath('/html/body/div/nav/div/ul[2]/li[1]')
    u.click()

  b = driver.find_element_by_xpath('/html/body/main/div/div[1]/button') # �V�K�O���[�v�{�^��
  b.click()

  ib = driver.find_elements_by_class_name("form-control")

  ib[0].click();  ib[0].clear(); ib[0].send_keys(name) # ���O
  ib[1].click();  ib[1].clear(); ib[1].send_keys(exp)  # ����

  add_btn = driver.find_element_by_xpath('//*[@id="group"]/div[2]/div/div/div[3]/button[2]')
  add_btn.click()


def del_user():

  # check driver
  try:
    driver
  except NameError:
    return

  if driver.title != "User":
    u = driver.find_element_by_xpath('/html/body/div/nav/div/ul[2]/li[2]')
    u.click()
    time.sleep(0.7)
  driver.execute_script("window.scrollTo(0, 0);")

  del_icn = driver.find_elements_by_class_name("fa-trash")
  del_icn[0].click()

  del_btn = driver.find_elements_by_class_name("btn-danger")
  del_btn[0].click()

def add_user(id, name, passwd):

  # check driver
  try:
    driver
  except NameError:
    return

  if driver.title != "User":
    u = driver.find_element_by_xpath('/html/body/div/nav/div/ul[2]/li[2]')
    u.click()

  b = driver.find_element_by_xpath('/html/body/main/div/div[1]/button') # �V�K���[�U�{�^��
  b.click()

  ib = driver.find_elements_by_class_name("form-control")

  ib[0].click();  ib[0].clear(); ib[0].send_keys(id)
  ib[1].click();  ib[1].clear(); ib[1].send_keys(name)
  ib[2].click();  ib[2].clear(); ib[2].send_keys(passwd)
  ib[3].click();  ib[3].clear(); ib[3].send_keys(passwd)

  select = Select(ib[4])
  time.sleep(0.2)
  select.select_by_index(0)
#  time.sleep(0.2)
#  ib[4].click();  ib[4].clear(); ib[4].send_keys("a")

  add_btn = driver.find_element_by_xpath('//*[@id="user"]/form/div/div/div[3]/button[2]')
  add_btn.click()

  chks = driver.find_elements_by_class_name("form-check-input")

def au(num):

  # check driver
  try:
    driver
  except NameError:
    return

  driver.execute_script("window.scrollTo(0, 0);")

  print ("[ LoginID, Password ]")
  for i in range(num):
    lid = randomname(8)
    pw = randomname(9)
    print (lid, pw)
    add_user(lid,randomname(6),pw)

def auf(fname):
  f = open(fname)
  dts = f.read()
  dtsl = dts.split("\n")
  ddd = dtsl[:-1]
  n = 0
  for d in ddd:
    if n > 0:
      lp = d.split(" ")
      lid = lp[0]
      pw = lp[1]
      add_user(lid, lid, pw)
    n += 1


def add_area(l, t, w, h, tm=1.0):

  pg.moveTo(l,t,tm)

  pg.dragRel(w,h,tm, button="left")

def test1():

  if driver.title == "Login":
    login()

  if driver.title != "Project":
    u = driver.find_element_by_link_text(PROJECT)
    u.click()

  while (driver.title != "Project"):
    time.sleep(0.1)

  time.sleep(0.1)

  selp = driver.find_element_by_xpath('//*[@id="project"]/table/tbody/tr/td[1]/span/a')
  selp.click()

  time.sleep(1.5)
  pg.click(300,300)
  pg.vscroll(1000)

  time.sleep(1.0)

  s = driver.find_element_by_xpath('//*[@id="editor"]/nav/ul/li[6]')
  s.click()

  time.sleep(0.5)

  add_area(792,458,184,140)

  s = driver.find_element_by_xpath('//*[@id="editor"]/nav/ul/li[7]')
  s.click()

def all(ts=1.0):

  # check driver
  try:
    driver
  except NameError:
    return

  standby()
  time.sleep(ts)
  job1()
  time.sleep(ts)
  job2()
  time.sleep(ts)
  job3()
  time.sleep(18)
  job4()
  time.sleep(1)
  job5()

def job5():

  # ����
  s = driver.find_elements_by_class_name("navbar-item")
  s[12].click()

def job1():

  # �}��\�ݒ�
  s = driver.find_elements_by_class_name("navbar-item")
  s[6].click()

  # �̈�ݒ�
  pg.click(300,300)
  pg.vscroll(1000)
#  add_area(795,460,180,100)
  add_area(1235,550,440,41)

  # �}��ݒ�
  s[7].click()

# �R�Â�
def job2():

  while(1):
    ib = driver.find_elements_by_class_name("list-group-item")
    if len(ib) > 0:
      break
    time.sleep(0.1)

  okbtn = driver.find_elements_by_class_name("btn-primary")

#  simg = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div[2]/div[3]/div[2]/div/div[1]/ul/li[1]/img')
#  for i in range(8):
#    ib[i].click()
#    simg.click()



  ib[0].click()
  time.sleep(0.5)
  simg = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div[2]/div[2]/div[2]/ul/li[1]/img')
  simg.click()
  okbtn[1].click()
  time.sleep(0.5)

  ib[1].click()
  time.sleep(0.5)
  simg = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div[2]/div[2]/div[2]/ul/li[1]/img')
  simg.click()
  okbtn[1].click()
  time.sleep(0.5)

  ib[2].click()
  time.sleep(0.5)
  simg = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div[2]/div[2]/div[2]/ul/li[8]/img')
  simg.click()
  okbtn[1].click()
  time.sleep(0.5)

  okbtn[0].click()

# �E���o���p�̈�ݒ�A�����E���o��
def job3():

  # �����`�E�����`
  s = driver.find_elements_by_class_name("navbar-item")
  s[8].click()


  # �̈�ݒ�
  pg.click(300,300)
  time.sleep(0.5)
  pg.vscroll(1000)
  time.sleep(0.5)
  pg.vscroll(-1800)   # to page 2

  add_area(1150,450,560,420, 2.0)

  time.sleep(0.5)

  # �����E���o��
  s = driver.find_elements_by_class_name("navbar-item")
  s[10].click()

def sclick(x,y):

  pg.moveTo(x,y)
  pg.mouseDown(button='left')
  time.sleep(0.1)
  pg.mouseUp(button='left')

# �蓮�ݒ�
def job4():

#  import pdb; pdb.set_trace()

  s = driver.find_elements_by_class_name("navbar-item")
  s[11].click()
  time.sleep(1.0)

  sclick(1315, 690)
  sclick(1470, 700)
  sclick(1580, 545)

def test2():

  if (driver.title != "Main"):
    print ("���̉�ʂł́A���s�ł��܂���!")
    return

  s = driver.find_element_by_xpath('//*[@id="editor"]/nav/ul/li[9]')
  s.click()

  time.sleep(0.5)

  x = 300
  y = 400
  yg = 100

  pg.click(x, y)

  for i in range(5):
    add_area(x, y,100,50,0.3)
    x = x + 20
    y = y + 100

  x = 1200
  y = 400
  yg = 100

  pg.click(x, y)

  for i in range(5):
    add_area(x, y,150,45,0.3)
    x = x - 20
    y = y + 100


def del_project():

  # check driver
  try:
    driver
  except NameError:
    return

  if driver.title == "Login":
    login()

  if driver.title != "Project":
    u = driver.find_element_by_link_text(PROJECT)
    u.click()

  driver.execute_script("window.scrollTo(0, 0);")

  time.sleep(0.5)

  del_icn = driver.find_element_by_xpath('//*[@id="project"]/table/tbody/tr[1]/td[6]/span/button[2]')
  del_icn.click()

  del_btn = driver.find_element_by_xpath('//*[@id="project"]/div[3]/div/div/div[3]/button[2]')
  del_btn.click()

def add_project(project_name, exp, pdf_path, wtime):

  # check driver
  try:
    driver
  except NameError:
    return

  if driver.title == "Login":
    login()

  if driver.title != "Project":
    u = driver.find_element_by_link_text(PROJECT)
    u.click()

  b = driver.find_element_by_xpath('/html/body/main/div/div[2]/button') # �V�K�v���W�F�N�g�{�^��
  b.click()

  fc = driver.find_elements_by_class_name("form-control")
  fc[0].click()
  fc[0].send_keys(project_name)

  fc[1].click()
  fc[1].send_keys(exp)

#  aa = driver.find_element_by_xpath("/html/body/main/div/div[3]/div/div/div[2]/div[3]/div[2]")
#  aa.click()

#  time.sleep(1.0)
#  pg.typewrite(pdf_path)
#  pg.press("enter")

  cfile = driver.find_elements_by_id("customFile")
  #fc[0].click()
  cfile[0].send_keys(pdf_path)

  # Page
  fc[2].click()
  fc[2].send_keys("36,37,38")

#  aa.send_keys(pdf_path)  # ���߂������B

  time.sleep(1.0)

  aa = driver.find_element_by_xpath('//*[@id="project"]/div[3]/div/div/div[3]/button[2]')  # �ǉ�

  time.sleep(wtime)

  aa.click()

  while(True):
    if driver.title != "Rotation":
      time.sleep(1.0)
    else:
      break

  okbtn = driver.find_elements_by_class_name("btn-primary")
  okbtn[0].click()

def ap_test(project_name, project_exp,  wtime = 5.0, llsw = False):

  if llsw == True:
    login()

  add_project(project_name, project_exp, "d:\\forRPA\\for_sc_test.pdf", wtime)

  if llsw == True:
    time.sleep(5.0)
    logout()

def standby():

  if driver.title == "Login":
    login()

  add_group ("a", "a")

  time.sleep(2.0)

  add_user("aaaaa","aaaaa","aaaaa")

  time.sleep(2.0)

#  add_project("test", "test", "d:\\forRPA\\for_sc_test.pdf", 6.0)
  add_project("test", "test", "d:\\forRPA\\sample.pdf", 6.0)

def setup():

  if driver.title == "Login":
    login()

  ap_test("a", "a")

def cleanup():

  # check driver
  try:
    driver
  except NameError:
    return

  if driver.title == "Login":
    login()

  del_user()

  del_project()
  time.sleep(1.0)

  del_group()

def cpos(cwin):

  global m_x
  global m_y

  # 10sec
  tl = 10.0
  for i in range(100):

    x = pg.position().x
    y = pg.position().y

    m_x = x
    m_y = y

    cwin.addstr(1,2, 'X ={x:4}, Y ={y:4}'.format(x=x,y=y))
    cwin.addstr(2,2, 'Remain time ={tl:5.1f}'.format(tl=tl))
    cwin.refresh()
    time.sleep(0.1)
    tl -= 0.1

  cwin.addstr(2,2, 'Time is up!        ')
  cwin.refresh()
  curses.curs_set(1)

def menu(stdscr):

  stdscr.clear()
  stdscr.addstr( 1,2,"----  Menu  ----")
  stdscr.addstr( 2,2,"0: Open Chrome")
  stdscr.addstr( 3,2,"1: login()")
  stdscr.addstr( 4,2,"2: logout()")
  stdscr.addstr( 5,2,"3: all()")
  stdscr.addstr( 6,2,"4: delete user()")
  stdscr.addstr( 7,2,"5: delete group()")
  stdscr.addstr( 8,2,"6: delete project()")
  stdscr.addstr( 9,2,"7: clean up()")
  stdscr.addstr(10,2,"8: disp cursor pos mode.")
  stdscr.addstr(11,2,"9: mouse click.")
  stdscr.addstr(12,2,"q: quit()")
  curses.curs_set(1)
  stdscr.border()
  stdscr.refresh()

def main(stdscr):


  menu(stdscr)

  while(1):
    key = stdscr.getkey()
    if key == '0':
      wopen()
      menu(stdscr)

    if key == '1':
      login()
    if key == '2':
      logout()
    if key == '3':
      all()
    if key == '4':
      del_user()
    if key == '5':
      del_group()
    if key == '6':
      del_project()
    if key == '7':
      cleanup()
    if key == '8':

      curses.curs_set(0)
      win = curses.newwin(4,22,14,22)
      win.border()

      t1 = threading.Thread(target=cpos, args=(win,))
      t1.start()

    if key == '9':
      pg.click(m_x, m_y)


    if key == 'q':
      break

if __name__ == "__main__":


  curses.wrapper(main)

  try:
    driver
  except NameError:
    sys.exit()

  driver.close()
  driver.quit()

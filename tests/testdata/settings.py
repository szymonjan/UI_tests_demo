from wtframework.wtf.config import WTF_CONFIG_READER

# The idea of a 'testdata' package is to organize your test data and test settings.
# While tests can reference the WTF_CONFIG_READER directly like this
#
#    admin_user = WTF_CONFIG_READER.get("admin_user", "admin")
#
# But you'll have the same hard coded "admin_user" string all over your tests.
# It is better to abstract that away into function calls so the same hard coded
# string isn't repeated throughout your code.  This creates a single point of
# maintenance for any config refactoring.
#
#
# This is an example of how you can uses a settings object.
# Here in your test, you can now refer to your admin login
# like this
#
#     login_page.login( get_admin_user(), get_test_admin_password() )
#
# Then when you run on different envionrments or different accounts,
# you can simply pass in a config file that'll specify the value for
# 'admin_user' and 'admin_password'


def url_address():
    "Application under test URL"
    return WTF_CONFIG_READER.get('test_data.url')

def login():
    "Correct login"
    return WTF_CONFIG_READER.get('test_data.login')

def password():
    "Correct password"
    return WTF_CONFIG_READER.get('test_data.password')

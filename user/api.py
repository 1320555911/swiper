# Create your views here.
from common import errors, keys
from lib.cache import rds
from lib.http import render_json
from lib.sms import send
from user.models import User


def fetch_vcode(request):
    '''给用户发送验证码'''
    phonenum = request.GET.get('phonenum')
    if not phonenum:
        return render_json(None,errors.PARAM_ERR)
    res = send(phone_numbers=phonenum)
    if res:
        return render_json(None)
    else:
        return render_json(None,errors.VCODE_FAILD)


def login(request):
    '''提交验证码，执行登录注册'''
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if not phonenum or not vcode:
        return render_json(None,errors.PARAM_ERR)
    key = keys.VCODE_K % phonenum
    cached_vcode = rds.get(key)
    if vcode==cached_vcode:
        user, created = User.objects.get_or_create(phonenum=phonenum,nickname=phonenum)
        request.session['uid'] = user.id
        return render_json(user.to_dict())
    else:
        return render_json(None,errors.VCODE_ERR)


def show_profile(request):
    return None


def update_profile(request):
    return None
# Create your views here.
from common import errors
from lib.http import render_json
from lib.sms import SMS


def fetch_vcode(request):
    phonenum = request.GET.get('phonenum')
    sms=SMS()
    res = sms.send(phone_numbers=phonenum)
    if res:
        return render_json(None,errors.OK)
    else:
        return render_json(None,400)


def login(request):
    return None


def show_profile(request):
    return None


def update_profile(request):
    return None
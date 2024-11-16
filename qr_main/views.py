from django.shortcuts import render, redirect
from .forms import QRCodeForm
import qrcode
import os
from django.conf import settings


def generate_qr_code(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            res_name = form.cleaned_data['restaurant_name']
            url = form.cleaned_data['url']
            
            # Generate QR Code
            qr = qrcode.make(url)
            # print(qr)
            file_name = res_name.replace(" ", "_").lower() + '_menu.png'
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            qr.save(file_path)
            
            # create image url
            qr_url = os.path.join(settings.MEDIA_URL, file_name)
            # print(qr_url) #/media/restauranto_menu.png
            
            '''
            # context = {
            #     'res_name':res_name,
            #     'qr_url': qr_url
            # }
            # return render(request, 'qr_result.html', context)
            '''
            
            # Store the generated data in the session
            request.session['res_name'] = res_name
            request.session['qr_url'] = qr_url
            request.session['file_name'] = file_name
            return redirect('qr_code_result')
            
    else:
        
        form = QRCodeForm()
        context = {
            'form': form
        }
        return render(request, 'generate_qr_code.html', context)




def qr_code_result(request):
    # Retrieve the data from the session
    res_name = request.session.get('res_name')
    qr_url = request.session.get('qr_url')
    file_name = request.session.get('file_name')

    # If the data is not in the session, redirect to the form page
    if not res_name or not qr_url:
        return redirect('generate_qr_code')

    context = {
        'res_name': res_name,
        'qr_url': qr_url,
        'file_name': file_name
    }
    return render(request, 'qr_result.html', context)

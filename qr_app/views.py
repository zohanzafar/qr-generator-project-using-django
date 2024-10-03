import io
import base64
from django.shortcuts import render
from .forms import QRCodeForm
from .utils import generate_qr_code
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            qr = generate_qr_code(url)
            img_buffer = io.BytesIO()
            qr.save(img_buffer, format='PNG')
            img_str = base64.b64encode(img_buffer.getvalue()).decode()
            return render(request, 'home.html', {'form': form, 'img_str': img_str})
    else:
        form = QRCodeForm()
    return render(request, 'home.html', {'form': form})
from django import forms

class Message_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
        'invalid': 'Isi input dengan hh:mm:ss',
    }
    attrs = {
        'class': 'form-control'
    }

    nama = forms.CharField(label='Nama Kegiatan', required=True, max_length=80,
                           empty_value='Anonymous', widget=forms.TextInput(attrs={'size': '80'}))
    tanggal = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required = True)
    jam = forms.TimeField(widget=forms.TimeInput(
        attrs={'type': 'time'}), required=True)
    tempat = forms.CharField(label='Tempat Kegiatan', widget=forms.TextInput(
        attrs={'size': '80'}), max_length=80, required=True)
    kategori = forms.CharField(label='Kategori Kegiatan', widget=forms.TextInput(
        attrs={'size': '80'}), max_length=80, required=True)

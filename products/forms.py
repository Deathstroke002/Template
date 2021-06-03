from django import forms 


from .models import Product


class ProductForm(forms.ModelForm):
	title 		= forms.CharField(label='', 
					widget=forms.TextInput(attrs={"placeholder": "Title"}))
	email = forms.EmailField()
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
								attrs={
								    "placeholder": "Describe",
									"Class": "new-class-name two",
									"id": "my-id-for-textareas",
									"rows": 20,
									'cols': 120,
								}
							)
						)
	price 		= forms.DecimalField(required=False, initial=199.99)
	class Meta:
		model = Product
		fields = {
		 	'title',
		 	'description',
		 	'price'
		}
	def clean_title(self, *args, **kwargs):
		title = self.cleaned_data.get("title")
		if not "CFE" in title:
			raise forms.ValidationError("This is not a vlaid title")
		return title
	
	def clean_titleemail(self, *args, **kwargs):
		email = self.cleaned_data.get("email")
		if not email.endswith("edu"):
			raise forms.ValidationError("Not a valid email")
		return email		

class RawProductForm(forms.Form):
	title 		= forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Title"}))
	description = forms.CharField(
						required=False, 
						widget=forms.Textarea(
								attrs={
								    "placeholder": "Describe",
									"Class": "new-class-name two",
									"id": "my-id-for-textareas",
									"rows": 10,
									'cols': 20,
								}
							)
						)
	price 		= forms.DecimalField(required=False, initial=199.99)
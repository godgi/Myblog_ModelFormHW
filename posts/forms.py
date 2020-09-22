from django.forms import ModelForm
from .models import Product


class PostForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'item',
            'explanation',
            'price',
            'stock',
            'image',
        ]

        labels = {
            'item': ('상품 이름'),
            'explanation': ('상품 설명'),
            'price': ('상품 가격'),
            'stock': ('상품 재고'),
            'image': ('이미지'),
        }

        help_texts = {
            'item': ('상품 이름을 입력해주세요'),
            'explanation': ('상품 설명을 입력해주세요'),
            'price': ('상품 가격을 입력해주세요'),
            'stock': ('상품 재고을 입력해주세요'),
        }
    def save(self, **kwarg):
        post = super().save(commit=False)
        post.user = kwarg.get('user', None)
        post.save()
        return post
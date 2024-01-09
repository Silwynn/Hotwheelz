from django.db import models

def upload_directory_path(instance, filename) -> str: 
    ext = filename.split('.')[-1]
    filename = f'{instance.id}_{instance}.{ext}'
    
    return f'uploads/{filename}'

# BaseModel to inherit created_at and updated_at fields
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        
class CarBrand(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CarModel(BaseModel):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_directory_path, blank=True)
    # Add other relevant fields (specifications, features, etc.)
    
    def __str__(self):
            return self.name
        
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            
            return self.image.url
        
        return "/media/uploads/default.jpg"
        
class Collection(BaseModel):
    name = models.CharField(max_length=100, null=True)
    cars = models.ManyToManyField(CarModel)
    # Add other relevant fields (purchase date, additional details, etc.)
    
    def __str__(self):
        return self.name or ''
    

class Owner(BaseModel):
    name = models.CharField(max_length=100, null=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)
    # Add other relevant fields (contact information, etc.)

    def __str__(self):
            return self.name
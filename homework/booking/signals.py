from .forms import SLOT_CHOICE
from django.core.mail import send_mass_mail
from django.db.models.signals import post_save
from .models import BookingModel
from django.dispatch import receiver

@receiver(post_save,sender=BookingModel)
def post_save_bookingmodel__sending_email(sender,instance,created,**kwargs):
        if created:
                cleaner_msg="You have Book for a Date "+str(instance.date)+" Time is "+SLOT_CHOICE[int(instance.timeslot)][1]+" for cleaning service at "+\
                        str(instance.city) + "\nCustomer name : "+ str(instance.user.first_name) +"\nCustomer Number : "+str(instance.user)+"\nSee Your Orders List :127.0.0.1:8000/bookorder/'"

                customer_msg="You have Book Cleaner "+str(instance.date)+" Time is "+SLOT_CHOICE[int(instance.timeslot)][1]+" for cleaning service at "+\
                        str(instance.city) + "\nCleaner name : "+ str(instance.cleaner.user.first_name) +"\nCleaner Number : "+str(instance.cleaner.user)+"\nSee Your Booked List :127.0.0.1:8000/booklist/"


                cleaner_mail  = ('You Booked', cleaner_msg, 'lalitvasoya.286@gamil.com', [instance.cleaner.user.email])
                customer_mail = ('You Book', customer_msg, 'lalitvasoya.286@gamil.com', [instance.user.email])
                # print("mail not send yet ")         
                res = send_mass_mail((cleaner_mail, customer_mail), fail_silently = False)
        else:
                raise("Not Booking")

from django.db import models

# Create your models here.


class Schedule(models.Model):
    test_bed=models.ForeignKey('tools.TestBed',on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(verbose_name="Date",null=False,blank=False)
    start_time = models.TimeField(default=None,null=False,blank=False,error_messages={'blank':'Starting time can not be empty'})
    end_time = models.TimeField(default=None,null=False,blank=False,error_messages={'blank':'Ending time can not be empty'})
    is_available = models.BooleanField(default=True,null=False,blank=False)

    class Meta:
        unique_together = (('date', 'start_time','end_time','test_bed'),)
        db_table = 'schedules'
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'

    def __str__(self):
        return "%s %s - %s" % (self.date.strftime('%m/%d/%Y'),self.start_time.strftime("%H:%M:%S"),self.end_time.strftime("%H:%M:%S"))
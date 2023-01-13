from django.db import models

# Create your models here.


class Project(models.Model):
    class Status(models.TextChoices):
        DATE_BOOKED = "DATE BOOKED", 'DATE BOOKED'
        DRAFT = "DRAFT", "DRAFT"
        PENDING = "PENDING","PENDING"
        COMPLETED = "COMPLETED","COMPLETED"

    owner = models.ForeignKey('users.User',on_delete=models.CASCADE, null=False, blank=False)
    name = models.CharField(max_length=255,blank=True,null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    diagram=models.ImageField(upload_to='uploads/projects/diagrams/', blank=True, null=True)
    extra_instruction=models.TextField(blank=True,null=True)
    schedule = models.ForeignKey('schedules.Schedule',on_delete=models.SET_NULL,blank=True,null=True)
    status = models.TextField(choices=Status.choices, default=Status.DATE_BOOKED)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)

    class Meta:
        db_table = 'projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return "%s %s" % (self.name, self.created_at.strftime("%m/%d/%Y, %H:%M:%S"),)


class ProjectTool(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE, blank=False,null=False)
    tool = models.ForeignKey('tools.Tool',on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    class Meta:
        db_table = 'project_tools'
        verbose_name = 'Project Tool'
        verbose_name_plural = 'Project Tools'

    def __str__(self):
        return "%s %s" % (self.project.name, self.tool.name,)
from django.db import models

# 평점을 만들어야.. 하나?
# 특정 모집단위에 대해 여러가지 정보를 작성을 한다면.... 해당 모집단위의 휴가일수, 하는일, 간단한 부대위치 및 교통
# 약간 방사형 그래프를 하나 보여주고 싶은데... 
# 뭐 평균휴가일수, 복무여건, 개인시간보장, 평균평점, 그리고무언가 이런식으로 해서 5각, 6각 그래프를 하나 뽝 보여주고싶은뎅
# post 에서 강제로 이것저것 설정을 하게 만들까? 점수를 주게 만들고 점수에따라서 Service에 apply 되는거지


class Service(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title


# Have to cosider about applying Field.unique_for_month option
class Cutline(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    score = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return str(self.date) + ' : '+str(self.score)

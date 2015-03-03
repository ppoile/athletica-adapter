from main import models

def fix_db_main():
    bad_serien = models.Serie.objects.filter(anlage_id=0)
    if bad_serien.count() > 0:
        bad_serien.update(anlage_id=None)
        print "model Serie fixed"
    else:
        print "model Serie is fine"

    bad_starts = models.Start.objects.filter(staffel_id=0)
    if bad_starts.count() > 0:
        bad_starts.update(staffel_id=None)
        print "model Start fixed"
    else:
        print "model Start is fine"

    bad_rundensets = models.Rundenset.objects.filter(hauptrunde=None)
    if bad_rundensets.count() > 0:
        bad_rundensets.update(hauptrunde=0)
        print "model Rundenset fixed"
    else:
        print "model Rundenset is fine"

    print "done"

from main import models

def fix_db_main(dry_run=False):
    bad_serien = models.Serie.objects.filter(anlage_id=0)
    if bad_serien.count() > 0:
        print "there are %d series with anlage_id=0..." % bad_serien.count(),
        if not dry_run:
            bad_serien.update(anlage_id=None)
            print "fixed"
        else:
            print
    else:
        print "series are fine"

    bad_starts = models.Start.objects.filter(staffel_id=0)
    if bad_starts.count() > 0:
        print "there are %d starts with staffel_id=0..." % bad_starts.count(),
        if not dry_run:
            bad_starts.update(staffel_id=None)
            print "fixed"
        else:
            print
    else:
        print "starts are fine"

    print "done"

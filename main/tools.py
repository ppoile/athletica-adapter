
def getWettkaempfe(meeting, event):
    licensed_event = False
    if event.endswith("*"):
        licensed_event = True
    kategorie = event.rstrip("*")

    kategorien_wettkaempfe = meeting.wettkaempfe.filter(
        kategorie__name=kategorie)
    if licensed_event:
        wettkaempfe = kategorien_wettkaempfe.exclude(
            mehrkampfcode=799)
    else:
        wettkaempfe = kategorien_wettkaempfe.filter(
            mehrkampfcode=799)
    return wettkaempfe

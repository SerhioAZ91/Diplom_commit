import sender_stand_reqest

current_track = sender_stand_reqest.track

def test_return_status_code():

    order_response = sender_stand_reqest.get_order_track(current_track)

    assert order_response.status_code == 200

    if order_response.status_code == 200:
        print("Ok")
    else:
        print("Is not Ok")

from french_toast.frying_pan import FryingPan


if __name__ == "__main__":
    pan = FryingPan('http://www.universalhub.com/toast.xml', 'status')
    print(pan.get_french_toast())


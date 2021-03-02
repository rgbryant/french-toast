from frying_pan import FryaingPan


if __name__ == "__main__":
    pan = FryingPan('http://www.universalhub.com/toast.xml', 'status')
    print(FryingPan.get_french_toast())


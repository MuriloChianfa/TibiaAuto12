import time

from core.HookWindow import LocateImage

CoinsImagePath = 'images/Items/Gold'


def ScanAutoExchangeGold(enabled_auto_exchange_gold, main_container_position, main_container_size, right_click):
    while True:
        ExchangePositions = [0, 0]
        MainContainerRegion = main_container_position[0], main_container_position[1], main_container_position[
            0] + main_container_size[0], main_container_position[1] + main_container_size[1]

        # look for platinum coins to exchange
        ExchangePositions[0], ExchangePositions[1] = LocateImage(
            f'{CoinsImagePath}/platinum.png', Precision=.92, Region=(MainContainerRegion))

        # look for gold coins to exchange only if platinum coins were not found
        if ExchangePositions[0] != 0 and ExchangePositions[1] != 0:
            ExchangePositions[0], ExchangePositions[1] = LocateImage(
                f'{CoinsImagePath}/gold.png', Precision=.9, Region=(MainContainerRegion))

        if ExchangePositions[0] == 0 and ExchangePositions[1] == 0:
            # break the loop if no exchangeable money found
            break
        else:
            # else, exchange money
            x = (
                main_container_position[0] + ExchangePositions[0])
            y = (
                main_container_position[1] + ExchangePositions[1]) + 24
            right_click(x, y)

        time.sleep(.3)

        if not enabled_auto_exchange_gold:
            break

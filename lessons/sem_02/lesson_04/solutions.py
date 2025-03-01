import numpy as np
from enum import Enum
from numbers import Real

# Task 1

class InconsistentDataError(Exception):
    pass

def get_most_profitable_month_name(
    amounts_of_sold_subscriptions: np.ndarray,
    subscriptions_prices: np.ndarray,
) -> str:

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    N = subscriptions_prices.size

    if amounts_of_sold_subscriptions.shape[1] != N:
        raise InconsistentDataError

    income = amounts_of_sold_subscriptions @ subscriptions_prices.reshape((N, 1))
    max_income_index = np.argmax(income)

    return months[max_income_index]

class Strategies(Enum):
    BY_GOOD = 0
    BY_MONTH = 1

def get_mean_profit(
    amounts_of_sold_subscriptions: np.ndarray,
    subscriptions_prices: np.ndarray,
    strategy: Strategies | None = None,
) -> np.ndarray | Real:

    N = subscriptions_prices.size

    if amounts_of_sold_subscriptions.shape[1] != N:
        raise InconsistentDataError

    incomes = np.multiply(amounts_of_sold_subscriptions, subscriptions_prices)

    match strategy:
        case Strategies.BY_GOOD:
            return (np.mean(incomes, axis=0)).flatten()
        case Strategies.BY_MONTH:
            return (np.mean(incomes, axis=1)).flatten()
        case None:
            income_by_month = np.sum(incomes, axis=1)
            return np.mean(income_by_month)
    
    return 0

def sort_month_names_by_profits(
    amounts_of_sold_subscriptions: np.ndarray,
    subscriptions_prices: np.ndarray,
    ascending: bool = True,
) -> list[str]:
    
    months = np.array(["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
    N = subscriptions_prices.size

    if amounts_of_sold_subscriptions.shape[1] != N:
        raise InconsistentDataError
 
    income = amounts_of_sold_subscriptions @ subscriptions_prices.reshape((N, 1))
    indices = np.argsort(income, axis=0).flatten()

    if (not ascending):
        indices = indices[::-1]
    
    return months[indices].tolist()


# Task 2
def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:

    if pad_size < 1:
        raise ValueError("Pad size must be greater than or equal to 1")

    match (image.ndim):
        case 2:
            rows, cols = image.shape
            new_rows, new_cols = rows + 2 * pad_size, cols + 2 * pad_size
            padded = np.zeros((new_rows, new_cols))
            padded[pad_size : (pad_size + rows), pad_size : (pad_size + cols)] = image
        case 3:
            rows, cols, rgb = image.shape
            new_rows, new_cols = rows + 2 * pad_size, cols + 2 * pad_size
            padded = np.zeros((new_cols, new_rows, rgb))
            padded[pad_size : (pad_size + rows), pad_size : (pad_size + cols), :] = image
        case _:
            raise ValueError("Image must be 2D or 3D")

    return padded

def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:

    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError("Kernel size must be an odd number greater than 1")

    padded = pad_image(image, kernel_size // 2)
    result = np.zeros_like(image)

    match (image.ndim):
        case 2:
            rows, cols = image.shape
            for i in range(rows):
                for j in range(cols):
                    blur_space = padded[i : (i + kernel_size), j : (j + kernel_size)]
                    result[i, j] = np.mean(blur_space)
        case 3:
            rows, cols, rgb = image.shape
            for i in range(rows):
                for j in range(cols):
                    blur_space = padded[i : (i + kernel_size), j : (j + kernel_size), :]
                    result[i, j, :] = np.mean(blur_space, axis=(0, 1))
        case _:
            raise ValueError("Image must be 2D or 3D")

    return result

# Task 3
def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:

    if threshold < 1:
        raise ValueError("Threshold must be greater than or equal to 1")

    all_image = np.unique_values(image)
    freq = np.zeros_like(all_image)

    for i in range(freq.size):
        freq[i] = np.sum(np.abs(all_image - all_image[i]) <= threshold)

    most_frequent = np.uint8(all_image[np.argmax(freq)])
    percent = float(np.max(freq) / image.size) * 100

    return most_frequent, percent
from nested_list import nested_list
import decorator


@decorator.give_log_path('logs/')
def flat_generator(list_):
    for item in list_:
        if type(item) is list:
            for sub_item in flat_generator(item):
                yield sub_item
        else:
            yield item


if __name__ == '__main__':

    for item in flat_generator(nested_list):
        print(item)

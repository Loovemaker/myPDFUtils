from pikepdf import Pdf
from easygui import textbox, msgbox
from tkinter.filedialog import askopenfilename, asksaveasfilename


def recognize_page_ranges(text: str, page_limit=None) -> [range]:
    if page_limit:
        assert page_limit > 0
    result = []

    expressions = text.split()
    for expression in expressions:
        try:
            args = [int(arg) for arg in expression.split('-')]
            if len(args) == 1:
                args += args
            args[1] += 1    # make human-readable closed ranges into default open ones
            assert args[0] > 0 and args[1] > 0, 'page number must be greater than zero'
            if page_limit:
                assert args[0] <= page_limit and args[1] <= (page_limit + 1), f'page number must be in page range (1 - {page_limit})'
            result.append(range(*args))
        except (ValueError, TypeError, AssertionError) as e:
            print(f'Warning: {expression} is ignored due to {e.__class__.__name__} ({e})')

    return result


def merge_page_ranges(ranges: [range]) -> set:
    result = set()

    for range in ranges:
        for page in range:
            result.add(page)
    return result


def get_pages(page_limit=None) -> set:
    msg = f'''
        使用任意Python风格的空字符（空格、回车、制表符等）进行分割；
        使用 - 表示闭区间范围；
        范围可以使用Python风格的步长功能；
        避免输入任何超过页码范围的数值（当前为 1 - {page_limit}）
        避免输入其它异常数据，避免意外绕过安全检查；
        
        例如：
            输入：1-5 3-8 10-15-2 20
            输出：1 2 3 4 5 6 7 8 10 12 14 20
    '''
    result = set()
    page_range_text = textbox(title='输入页码范围', msg=msg)
    if page_range_text:
        page_ranges = recognize_page_ranges(page_range_text, page_limit)
        result = merge_page_ranges(page_ranges)

    if not result:
        msgbox(title='❌错误', msg='未找到有效数据')
    else:
        msgbox(title='识别结果', msg=f"这是识别到的页码数据，请确认：\n\n{' '.join([str(page) for page in result])}")

    return result


if __name__ == '__main__':

    path_open = askopenfilename(title='打开PDF文件', defaultextension='pdf')
    if not path_open:
        exit()
    with Pdf.open(path_open, allow_overwriting_input=True) as pdf:
        targets = get_pages(page_limit=len(pdf.pages))

        for target in reversed(list(targets)):   # avoid index dislocation
            i = target - 1
            del pdf.pages[i]

        path_save = asksaveasfilename(title='保存PDF文件', defaultextension='pdf')
        if not path_save:
            exit()
        pdf.save(path_save)

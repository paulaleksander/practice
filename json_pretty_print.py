
class PrettyPrint:

  def __init__(self, unparsed_string):
    self.unparsed_string = unparsed_string
    self.tabs = '    '
    self.tabs_amount = 0

  def string_split(self):

    new_p = self.unparsed_string[1:]
    splitted_unparsed_string = new_p.split(', ')
    opener = self.unparsed_string[0]
    splitted_unparsed_string.insert(0, opener)
    ender_row = splitted_unparsed_string[-1]
    ender = ender_row[-1]
    splitted_unparsed_string[-1] = splitted_unparsed_string[-1][:-1]
    splitted_unparsed_string.append(ender)
    return splitted_unparsed_string

  def print_op_brace(self, string):
    open_square_brace_i = string.find('[')
    open_curle_brace_i = string.find('{')
    open_braces = []
    if open_square_brace_i > -1:
      open_braces.append(open_square_brace_i)
    if open_curle_brace_i > -1:
      open_braces.append(open_curle_brace_i)
    open_brace_index = min(open_braces)
    print(self.tabs * self.tabs_amount + string[:open_brace_index+1])
    brace_open_count = string.count('[') + string.count('{')
    for i in range(brace_open_count - 1):
      self.tabs_amount += 1
      print(self.tabs * self.tabs_amount + string[open_brace_index+1 + i]) 

    post_brace_index = open_brace_index + brace_open_count
    self.tabs_amount += 1

    print(self.tabs * self.tabs_amount + string[post_brace_index:] + ',')

  def print_cl_brace(self, string):
    close_square_brace_i = string.find(']')
    close_curle_brace_i = string.find('}')
    close_braces = []
    if close_square_brace_i > -1:
      close_braces.append(close_square_brace_i)
    if close_curle_brace_i > -1:
      close_braces.append(close_curle_brace_i)
    close_brace_index = min(close_braces)
    print(self.tabs * self.tabs_amount + string[:close_brace_index])
    for i in string[close_square_brace_i:]:
      self.tabs_amount -= 1
      print(self.tabs * self.tabs_amount + i + ',')
  
  def parse(self):
    splitted_unparsed_string = self.string_split()

    for index, value in enumerate(splitted_unparsed_string):
      if value == '{' or value == '}':
        print(value)
        self.tabs_amount += 1
      else:
        brace_close_count = value.count(']') + value.count('}')
        brace_open_count = value.count('[') + value.count('{')
        if brace_close_count > 0:
          self.print_cl_brace(value)
        elif brace_open_count > 0:
          self.print_op_brace(value)
        elif value.find('[') == -1 and value.find('{') == -1:
          penultimate = len(splitted_unparsed_string) - 2
          if index == penultimate:
            print(self.tabs + value)
          else:
            print(self.tabs * self.tabs_amount + value + ',')



pukpold = '{"two": "3", "b": 123, "third": "3", "ce_kurwa": [123, {"asa": 1, "kek": [2, b]}, [1, 2, 3, 4, [[[9, 8]], -8]]], "ha": "haha"}'
new_pukpold = PrettyPrint(pukpold)
new_pukpold.parse()
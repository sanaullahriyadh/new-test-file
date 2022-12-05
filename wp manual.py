from make_wp_function import wp_p
from make_wp_function import wp_h2

first_peragraph_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."


heading_two_text = "Heading two"

second_paragraph_text = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."

article = wp_p(first_peragraph_text)+wp_h2(heading_two_text)+wp_p(second_paragraph_text)

print(article)
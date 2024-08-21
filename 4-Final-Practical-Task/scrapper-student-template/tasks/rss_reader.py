import html
import json as jsk
from argparse import ArgumentParser
from typing import List, Optional, Sequence, Dict
import requests


class UnhandledException(Exception):
    pass


def extract_tag_content(start_pos: int, xml: str, tag: str):
    start = f"<{tag}>"
    stop = f"</{tag}>"

    info_start = xml.find(start, start_pos) + len(start)
    if info_start == len(start) - 1:
        return None
    info_stop = xml.find(stop, start_pos)

    content = xml[info_start: info_stop]
    return html.unescape(content)


def extract_categories(xml: str, start_pos: int) -> List[str]:
    categories = []
    pos = start_pos
    while True:
        start_tag = xml.find("<category", pos)
        if start_tag == -1:
            break
        end_tag = xml.find("</category>", start_tag) + len("</category>")
        category_content = xml[start_tag:end_tag]
        category_value = extract_tag_content(0, category_content, "category")
        if category_value:
            categories.append(category_value)
        pos = end_tag
    return categories


def extract_channel_data(xml: str):
    tags = ["title", "link", "description", "lastBuildDate", "pubDate", "language", "managingEditor"]
    result = dict()
    for tag in tags:
        content = extract_tag_content(0, xml, tag)
        if content is not None:
            result[tag] = content
    categories = extract_categories(xml, 0)
    if categories:
        result["category"] = categories
    return result


def extract_items_data(xml: str) -> List[Dict[str, str]]:
    item_start = xml.find("<item>")
    item_stop = xml.find("</item>", item_start)
    tags = ["title", "author", "pubDate", "link", "description"]
    result = []
    while item_start != -1:
        cur_item = dict()
        for tag in tags:
            content = extract_tag_content(item_start, xml, tag)
            if content is not None:
                cur_item[tag] = content
        categories = extract_categories(xml, item_start)
        if categories:
            cur_item["category"] = categories
        result.append(cur_item)
        item_start = xml.find("<item>", item_stop)
        item_stop = xml.find("</item>", item_start)
    return result


def rss_parser(
        xml: str,
        limit: Optional[int] = None,
        json: bool = False,
) -> List[str]:
    channel_data = extract_channel_data(xml)
    items = extract_items_data(xml)

    if limit is not None:
        items = items[:limit]

    if json:
        output = channel_data
        if items:
            output["items"] = items

        return [jsk.dumps(output, indent=2, ensure_ascii=False)]

    output = []

    channel_keys = [
        "title",
        "link",
        "lastBuildDate",
        "pubDate",
        "language",
        "category",
        "managingEditor",
        "description"
    ]

    channel_templates = {
        "title": "Feed: {}",
        "link": "Link: {}",
        "lastBuildDate": "Last Build Date: {}",
        "pubDate": "Publish Date: {}",
        "language": "Language: {}",
        "category": "Categories: {}",
        "managingEditor": "Editor: {}",
        "description": "Description: {}"
    }

    for key in channel_keys:
        if key in channel_data:
            if key == "category":
                output.append(channel_templates[key].format(', '.join(channel_data[key])))
            else:
                output.append(channel_templates[key].format(channel_data[key]))
    output.append("")

    item_keys = [
        "title",
        "author",
        "pubDate",
        "link",
        "category",
        "description"
    ]

    item_templates = {
        "title": "Title: {}",
        "author": "Author: {}",
        "pubDate": "Published: {}",
        "link": "Link: {}",
        "category": "Categories: {}",
        "description": "{}"
    }

    for item in items:
        for key in item_keys:
            if key in item:
                if key == "category":
                    output.append(item_templates[key].format(', '.join(item[key])))
                else:
                    output.append(item_templates[key].format(item[key]))
            if key == "description":
                output.append("")
        output.append("")

    return output


def main(argv: Optional[Sequence] = None):
    """
    The main function of your task.
    """
    parser = ArgumentParser(
        prog="rss_reader",
        description="Pure Python command-line RSS reader.",
    )
    parser.add_argument("source", help="RSS URL", type=str, nargs="?")
    parser.add_argument(
        "--json", help="Print result as JSON in stdout", action="store_true"
    )
    parser.add_argument(
        "--limit", help="Limit news topics if this parameter provided", type=int
    )

    args = parser.parse_args(argv)
    xml = requests.get(args.source).text
    try:
        print("\n".join(rss_parser(xml, args.limit, args.json)))
        return 0
    except Exception as e:
        raise UnhandledException(e)


if __name__ == "__main__":
    main()
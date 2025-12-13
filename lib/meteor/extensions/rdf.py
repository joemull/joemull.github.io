import json
import os

import ark
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, SDO


SITE_GRAPH = Graph()


def add_via_site_graph(g: Graph, page_data: dict, data: str, a: URIRef) -> None:
    if not SITE_GRAPH.value(predicate=RDF.type, object=a, any=True):
        SITE_GRAPH.parse(data=data, format="turtle")
    for s, p, o in SITE_GRAPH:
        g.add((s, p, o))


def add_webpage_to_graph(g: Graph, page_data: dict) -> None:
    node = page_data["node"]
    site = g.value(predicate=RDF.type, object=SDO.WebSite, any=False)
    path = ark.site.out("")
    node_path = ark.utils.rewrite_urls(f"'{node.url}'", path).strip("'")
    page = URIRef(os.path.join(str(site), node_path))
    g.add((page, RDF.type, SDO.WebPage))
    if node_path.startswith("blog"):
        g.add((page, RDF.type, SDO.BlogPosting))
    g.add((page, SDO.isPartOf, site))
    author = g.value(subject=site, predicate=SDO.author, any=False)
    g.add((page, SDO.author, author))
    g.add((page, SDO.copyrightHolder, author))
    if node.get("title"):
        g.add((page, SDO.headline, Literal(node.get("title"))))
    g.add((page, SDO.license, Literal(ark.site.config.get("license", ""))))
    g.add((page, SDO.inLanguage, Literal("en")))
    if node.get("word_count"):
        g.add((page, SDO.wordCount, Literal(node.get("word_count", 0))))
    url = Literal(os.path.join(str(site), node_path))
    g.add((page, SDO.url, url))
    if node.get("date"):
        g.add((page, SDO.dateCreated, Literal(node.get("date"))))


# JSON-LD generation event
@ark.events.register(ark.events.Event.RENDER_PAGE)
def create_json_ld(page_data: dict) -> str:
    g = Graph()
    add_via_site_graph(g, page_data, data=ark.site.config["site_ttl"], a=SDO.WebSite)
    add_via_site_graph(g, page_data, data=ark.site.config["author_ttl"], a=SDO.Person)
    add_webpage_to_graph(g, page_data)
    json_ld_g = g.serialize(
        format="json-ld",
        context={"schema": SDO._NS},
        auto_compact=True,
    )
    json_ld_g = json.dumps(json.loads(json_ld_g), separators=(",", ":"))
    page_data["json_ld"] = json_ld_g
    return page_data

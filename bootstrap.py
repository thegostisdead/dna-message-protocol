from encoder.encoder import Encoder
from utils.utils import Utils
from factories import HelixFactory
from rich import print
from viewer import view

parsed_args = Utils.parse_args()
print(parsed_args)

print("[bold magenta]Message a convertir:[/bold magenta]", parsed_args.message)
ascii_sequence = Encoder.encode(parsed_args.message)
print("[bold magenta]Séquence a encoder :[/bold magenta]", ascii_sequence)

helix = HelixFactory.get_helix(is_redundant=parsed_args.redundant)

helix.add_message(ascii_sequence)

Utils.dump(helix.get_helix())
print(helix.get_message())

viewer = view(800, 360 * (len(helix.data) + 3), helix.get_message(), helix,
              parsed_args.output)

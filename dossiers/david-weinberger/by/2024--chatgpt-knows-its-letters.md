---
title: "chatGPT knows its letters"
person: david-weinberger
section: by
type: blog-post
year: 2024
date: 2024-03-27
venue: "Joho the Blog (hyperorg.com)"
authors: "David Weinberger"
source_url: https://hyperorg.com/2024/03/27/chatgpt-knows-its-letters/
retrieved: 2026-08-13
content: full-text
notes: "Post from Joho the Blog (hyperorg.com), Weinberger's personal blog. Retrieved via the site's WordPress REST API; HTML converted to plain text."
---

# chatGPT knows its letters

## Full text

A friend on a mailing list pointed to the massive palindromic story “2002” by Nick Montfort and William Gillespie, posted on Feb. 20. 2002, AKA 20-02-2002. It’s 2002 words long. And while it’s not exactly a great read, it is an amazing accomplishment.

So, I asked chatGPT to confirm that “it’s”2002” is an accurate palindrome. It confirmed it.

Then I asked it to write a palindromic story, saying it could be quite short. It came up with:

"Eva, can I see bees in a cave?"

When I asked it to write the next palindromic sentence, it came up with:

“Eva, can I see bees in a cave? Eva, can I see bees in a cave?”

which it acknowledged is maybe too simple a way out:

This repetition isn’t the most creative continuation, but it maintains the palindromic structure. Creating a palindromic story with varied content while preserving the integrity of the palindrome is an intricate endeavor, usually resulting in very simple and repetitive narratives. The key challenge lies in the reversal of letters and sounds, which typically leads to mirrored sentences rather than continued narrative development.

This was interesting to me, because the Large Language Models that produce chat AI applications like chatGPT turn the words they’re being trained on into tokens, which are unique numeric labels for each word, but also for strings of words, parts of words, punctuation, etc. So, when chatGPT is processing a prompt that contains the word “bees” it recognizes that as a particular token number. But you need to know about the actual letters, not just the token number, to construct a palindrome. So hat’s going on?

In this case, there’s a way around this seeming limitation (which we’ll see in a minute isn’t actually a limitation): “Eva, can I see bees in a cave?” exists on the Web as an example of a palindrome. So perhaps chatGPT didn’t construct it out of nothing.

But when given:

“mom bird rib taco cat taco cat bird rib mom”

it identifies it as a palindrome even though that phrase is a sort of googleWhack: it gets zero hits on Google.

When given the entire “2002” text, and asked if it’s a palindrome, chatGPT confidently says that it is.

It also correctly says:

“mom bird rib tackle cat taco cat bird rib mom”

is not a palindrome, and points to the exact error.

So, I asked chatGPT how it recognizes patterns in letters the compose a word, it replied:

Even though my processing of text is based on tokens, these tokens include representations for individual letters, words, and punctuation marks, which allows me to analyze and generate text based on specific linguistic rules and patterns, including identifying palindromic structures.

A good answer. Or an excellent hallucination.

And since it was my friend Drew’s grandma who pointed out “2002” to her, I can conclude:

An answer, Drew’s Nana!

PS: No, my friend isn’t really named Drew. So sue me!

PPS: In case you’re wondering why the formatting of chatGPT’s responses are so inconsistent in this post, it’s because WordPress’ “Gutenberg” block editor is an enshittification of their plain old editor. But ChatGPT guided me to the “classic” block in the Block editor, and I’ll be making a more thorough switch back to classic. I’m just too annoyed to fix the formatting on this particular post.

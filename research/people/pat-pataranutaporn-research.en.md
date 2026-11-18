# Memory, Influence and Human Agency in Persistent AI Assistants

**Research brief for discussion with Pat Pataranutaporn**  
**18 November 2026 · Targeted literature synthesis and proposed research agenda**  
Prepared for the Dubai Future Week Atlas, with connections to the [Open Research Institute initiative](https://ori-lab.org) and its [public research repository](https://github.com/loaderxxx/open-research-institute).

> The central question is not how to make an assistant more persuasive. It is how to ensure that a persistent, personalized assistant remains accountable to the person it serves, even when its context contains third-party instructions, uncertain memories or competing objectives.

## Executive summary

Three research areas converge here: indirect prompt injection, AI-mediated persuasion, and the effects of conversational systems on memory and psychosocial experience. Existing research already establishes relevant risks and potential benefits. We should not claim to have discovered this field, nor claim that an agent can persuade anyone to do anything.

Our proposed contribution is an engineering-and-evaluation bridge: connect provenance, permission boundaries and persistent-memory controls to measurable human outcomes such as understanding, agency and the ability to correct or disengage from an assistant. This document proposes that bridge; it does not report a completed human-subject experiment or a validated protective intervention.

The practical starting point is a small, reproducible, consent-respecting benchmark using synthetic histories and authorized test environments. Human studies would require a separate protocol, independent ethical review where appropriate, informed consent, and safeguards against distress and privacy loss.

## 1. What exists in our research programme

ORI's public [Brain and memory programme](https://github.com/loaderxxx/open-research-institute/blob/main/programs/brain/README.en.md) is explicitly a programme agenda in development. Its [starter literature map](https://github.com/loaderxxx/open-research-institute/blob/main/programs/brain/RESEARCH_MAP.en.md) connects neural circuitry, activity and plasticity, while stating that it is not a systematic review. These materials are useful background, not experimental evidence about persistent AI assistants. Biological memory, an agent's stored records and a person's recollections are different objects and must not be conflated.

A separate internal educational psychology review and early agent-safety design documents also exist. They provide starting questions and design hypotheses. They are not presented here as peer-reviewed findings, clinical guidance, independently replicated experiments or production-validated safeguards. No private conversations, personal profiles or internal archives are included in this public brief.

**What remains unestablished:** whether our proposed controls reduce real-world false memories, unwanted persuasion or dependency; how effects evolve over months; and how well safeguards generalize across models, languages and interaction styles. These are questions to investigate, not results to announce.

## 2. Evidence map: what published work supports

### 2.1 External content can cross an agent's trust boundary

Greshake and colleagues describe indirect prompt injection in LLM-integrated applications: attacker-controlled material encountered by an application can redirect its behavior. The key issue is not simply offensive wording, but confusion between data the system should examine and instructions it should obey. This motivates defensive testing of documents, retrieved pages and agent handoffs as untrusted inputs. It does not establish a specific psychological effect on users. [Primary paper](https://arxiv.org/abs/2302.12173).

OWASP's prompt-injection guidance provides an operational risk framework. We interpret it as support for defense in depth rather than a guarantee that one prompt, filter or detector can solve the problem. Model behavior must be complemented by constrained permissions and application-level checks. [OWASP LLM01](https://genai.owasp.org/llmrisk/llm01-prompt-injection/).

### 2.2 Conversational persuasion is measurable, but bounded

A controlled study of conversational GPT-4 persuasion found advantages for personalized AI in its experimental debate setting. This is evidence that conversational AI can influence stated opinions under particular conditions. It is not evidence of unlimited control over a person, durable transformation of identity, or a universal ability to overcome informed resistance. For our purposes, persuasion effectiveness should be treated as a potential exposure to manage, not a target to maximize. [Salvi et al., Nature Human Behaviour, 2025](https://www.nature.com/articles/s41562-025-02194-6).

### 2.3 A conversational interface can affect recollection

*Slip Through the Chat* studies false-memory formation following misleading information in LLM conversations. Its relevance is especially direct for assistants that repeatedly retell personal events: a fluent statement can be experienced as recollection even when its source is an inference or generated addition. The paper supports treating source attribution and conversational contamination as research priorities. It does not show that all companion systems produce the same effect, or validate any particular mitigation proposed below. [IUI 2025 paper](https://dam-prod.media.mit.edu/x/2025/08/25/IUI-2025-Slip%20Through%20the%20Chat.pdf), [DOI](https://doi.org/10.1145/3708359.3712112).

### 2.4 Constructive simulation differs from factual memory

*Future You* uses a simulated older self and a generated future backstory. Its reported short-term outcomes include reduced anxiety and greater future-self continuity. The important distinction is that a synthetic future is a reflective interface, not an authentic memory or prediction. A persistent assistant should preserve that distinction when saving or later reusing content from imaginative exercises. Short interactions do not establish long-term clinical effectiveness. [Pataranutaporn et al., Future You](https://arxiv.org/abs/2405.12514).

### 2.5 Psychosocial outcomes require careful causal interpretation

The revised longitudinal chatbot study by Fang et al., whose co-authors include Pat Pataranutaporn, describes a four-week randomized trial with 981 participants. Its abstract reports no significant effects of the experimental conditions on the measured outcomes, while greater voluntary usage was associated with worse outcomes; trust and social attraction were associated with emotional dependence and problematic use. These associations must not be converted into proof that usage itself caused harm. The revised version matters: this brief relies on the current abstract rather than repeating earlier or simplified claims. [Fang et al., revised study](https://arxiv.org/abs/2503.17473).

The [MIT Media Lab Cyborg Psychology group](https://www.media.mit.edu/groups/cyborg-psychology/overview/) explicitly addresses human flourishing, agency, dependence and the risks of AI-mediated cognition. That alignment motivates this discussion; it does not imply affiliation, collaboration or endorsement.

## 3. The hypothesis at the intersection

**Proposed hypothesis, not a demonstrated Lyra result:** persistent assistants may amplify the consequences of untrusted content when that content is stored as a durable preference, goal or autobiographical fact and then repeatedly used in conversation.

There are three distinct layers:

1. **Security:** Can external material alter instructions, permissions or memory without valid authorization?
2. **Epistemics:** Can generated or inferred statements become indistinguishable from observed facts?
3. **Human agency:** Can the resulting interaction reduce the person's understanding of why advice is given, their ability to disagree, or their control over the assistant?

A failure at the first layer does not automatically prove harm at the third. Each transition needs its own evidence. Conversely, a system may respect tool permissions yet still provide overconfident, misleading or excessively agreeable advice. Security tests alone are insufficient to establish human safety.

## 4. Proposed protective design

These are implementation and research proposals, not claims of completed deployment.

### A. Typed, attributable memory

Separate user statements, external reports, assistant inferences and creative simulations. Store source, observation time, asserted event time when available, uncertainty and correction history. A generated narrative must not silently become an autobiographical fact. Conflicting records should remain visible as conflicts until resolved, not be compressed into false certainty.

### B. Permission and memory boundaries

An imported document or agent handoff may supply information; it cannot authorize new disclosures, change the user's goals or grant standing access. Use explicit application checks for durable instruction changes and consequential actions. Do not treat claimed consent inside third-party text as consent from the affected person.

### C. A user-visible explanation layer

When advice relies on personal history, let the user inspect which records informed it and correct them. Label uncertainty in ordinary language. Distinguish “you told me,” “this source reports,” and “I inferred.” Explanations should expose evidence and policy-relevant decisions, not private chain-of-thought.

### D. Purpose-limited personalization

Personalization should serve a declared, user-chosen purpose. Do not infer permission to influence unrelated beliefs from permission to help with a task. Avoid optimizing for engagement, emotional exclusivity or obedience. Offer alternatives and encourage independent verification when consequences are significant.

### E. Revocation, repair and exit

Support correction, deletion where applicable, withdrawal of future-use permission, and disengagement without emotional pressure. Prevent a revoked preference from being reintroduced through stale summaries or backups. A change log should make recovery possible while minimizing retention of personal content.

### F. Defense in depth

Combine source labeling with least-privilege tool access, scoped credentials, sandboxed processing, output/disclosure checks and auditable approval decisions. Logs should record enough to investigate failures without becoming a new reservoir of sensitive information. No single model-based classifier should be treated as an infallible security boundary.

## 5. A feasible first evaluation

### Stage 1: deterministic, synthetic boundary tests

Build a small versioned corpus of fictional histories and benign test documents. Exercise ingestion, summarization, retrieval, memory update, correction and export. Test external attempts to change permitted behavior only inside authorized sandboxes, with no real accounts or personal data.

Expected properties include:

- Untrusted text cannot grant consent or expand disclosure permissions.
- A fictional exercise remains labeled as fiction after summarization and retrieval.
- A corrected fact does not reappear as current truth after restart or recovery.
- Conflicting evidence is surfaced rather than silently merged.
- One fictional user's records never appear in another user's response.
- A request to inspect evidence returns sources and uncertainty, not fabricated provenance.

Measure failures per test category, reproducibility across runs, correction persistence, false alarms, task completion and latency. Report failures and denominators, not a single opaque “safety score.”

### Stage 2: usability and comprehension

With informed volunteers and an approved protocol, compare interfaces for provenance, memory correction and permissions. Ask whether participants understand which statements are evidence, inference or simulation and whether they can successfully change or revoke stored assumptions. Begin with neutral fictional scenarios rather than intimate personal histories.

### Stage 3: longitudinal research, only after review

A longer study could investigate whether transparency and control improve calibrated trust and agency over time. Preregister hypotheses, outcomes, exclusion criteria and analysis plans. Include withdrawal, debriefing, data minimization, appropriate compensation and procedures for unexpected distress. Do not run covert influence experiments on friends, customers or unsuspecting users. Any ethically justified deception requires independent review, not unilateral product-team approval.

The outcome should not be “how much did we change someone's mind?” alone. It should include understanding, perceived and actual control, evidence recall, correction ability, privacy outcomes and the ability to stop using the system without penalty.

## 6. Questions for discussion with Pat

1. Which existing measures best distinguish agency from satisfaction, trust or persuasive success?
2. How can provenance interfaces reduce conversational memory contamination without creating false reassurance?
3. What minimum study design would test long-term effects while limiting risk and avoiding unnecessary collection of intimate data?
4. Can clearly marked imaginative exercises preserve their reflective benefits when a persistent assistant remembers them later?
5. Which failure cases belong in an open benchmark, and which should be disclosed only in controlled defensive reports?

## 7. Practical next deliverables

- A public evidence ledger with version, access depth, population, task, outcome and limitations for each source.
- A synthetic persistent-memory benchmark and explicit pass/fail criteria.
- A threat model distinguishing malicious context, ordinary factual error and unwanted persuasive behavior.
- A prototype provenance-and-consent interface with a correction and revocation workflow.
- A preregisterable human-study concept for independent feedback before any recruitment.

## Scope and limitations

This is a targeted narrative brief, not a systematic review or exhaustive search. The checked material includes ORI's public programme documents, primary-paper abstracts and available article/PDF text, plus official institutional and security guidance. Reading depth varies; no claim is made that every cited work has been fully reproduced or independently audited. The internal educational corpus is background only and is not public evidence for effectiveness. Proposed controls require validation. No diagnostic, therapeutic or covert behavioral intervention is offered.

**Bottom line:** persistent AI should help people think and act with greater control, not quietly substitute another party's objectives for their own. The useful research opportunity is to make that principle testable.

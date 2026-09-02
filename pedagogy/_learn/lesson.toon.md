id: AgentCore
gloss: production-runtime-and-policy-for-agents
why: Job-seeking as AI agent engineer. Friday workshop triad is sandbox plus toolkit plus Cedar.
probe: In your own words: what is Amazon Bedrock AgentCore, and what is it not?
expect: bedrock platform agents production not a model not a lebenslauf job gateway policy
claim: AgentCore is a Bedrock platform. Policy intercepts tool calls at Gateway. Cedar is point-in-time deny-by-default. Dogwood can use session history.
claim: AWS Compute Blog names three pieces that must work together for sandboxed coding agents: Lambda MicroVMs, Agent Toolkit for AWS, and Policy in AgentCore.
claim: Worked example: agent builds inside a MicroVM, then calls a deploy tool on Gateway with environment production. Cedar denies because the agent may only deploy to staging.
claim: Agent Toolkit is curated SKILL.md plus a managed AWS MCP Server. Product page names Kiro, Claude Code, Codex, MCP-compatible agents.
claim: Lambda MicroVMs are Firecracker-isolated session compute. The toolkit skill also names multi-tenant CI executors. Do not claim this repo already runs that.
neighbor: AgentToolkit
neighbor: LambdaMicroVM
neighbor: Agent
neighbor: AgentLoop
neighbor: AWS
neighbor: Bedrock
neighbor: MCP
neighbor: CursorSkill
neighbor: GitHubCI
source: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html
source: https://aws.amazon.com/blogs/compute/secure-code-execution-for-ai-agents-with-aws-lambda-microvms/
source: https://aws.amazon.com/products/developer-tools/agent-toolkit-for-aws/
source: CPU.md
drill: Which three pieces does AWS say must work together so a coding agent can build and deploy without improvising IAM or shipping to production? | microvm toolkit policy | mc | Lambda MicroVMs + Agent Toolkit + AgentCore Policy | ECS + SQS + CDK | LangGraph + CrewAI + AutoGen | Kafka + Redis + Sentry
drill: In the AWS worked example, the agent asks Gateway to deploy with environment production. What does Cedar do? | deny | mc | allow and log | deny because only staging is permitted | ask the human in Slack | retry with Dogwood
drill: Agent Toolkit for AWS is which kind of thing? | skill | mc | a Person vertex on this graph | curated skills plus a managed AWS MCP Server | a Kafka cluster | a lebenslauf job line
drill: Name one attested tool already on the lebenslauf that the Agent Toolkit product page also names. | kiro claude mcp | short
